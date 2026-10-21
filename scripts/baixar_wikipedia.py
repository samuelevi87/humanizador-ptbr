"""
baixar_wikipedia.py

Baixa artigos da Wikipédia lusófona na última revisão anterior a 30/11/2022
(lançamento do ChatGPT) e salva só os parágrafos de prosa, como texto humano
de controle para o corpus do humanizador-ptbr.

Cada arquivo sai em corpus/humano/wikipedia/<slug>.md com cabeçalho de
atribuição (título, oldid, data da revisão e licença CC BY-SA 4.0).

Uso: python scripts/baixar_wikipedia.py
"""
import json
import re
import ssl
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

API = "https://pt.wikipedia.org/w/api.php"
# Política da Wikimedia exige User-Agent identificável
USER_AGENT = "humanizador-ptbr-corpus/0.1 (https://github.com/; uso de pesquisa)"
CORTE = "2022-11-29T23:59:59Z"

# No Windows, a loja de certificados do sistema pode ter raízes vencidas; o pacote
# certifi, quando instalado, traz uma cadeia atualizada. A verificação continua ligada.
try:
    import certifi
    CONTEXTO_SSL = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    CONTEXTO_SSL = ssl.create_default_context()
DESTINO = Path(__file__).resolve().parent.parent / "corpus" / "humano" / "wikipedia"

# Artigos variados em tema para que o controle não fique enviesado para um assunto só.
# Temas escolhidos para espelhar os textos que serão gerados por IA (empresas,
# tecnologia, lugares, pessoas, economia).
ARTIGOS = [
    "Blumenau", "Embraer", "Natura &Co", "Pix (sistema de pagamento)", "Linux",
    "Aprendizado de máquina", "Computação em nuvem", "Santos Dumont", "Clarice Lispector",
    "Oscar Niemeyer", "Copa do Mundo FIFA de 2014", "Plano Real", "Floresta Amazônica",
    "Café", "Mercado Livre", "Nubank", "Petrobras", "Python", "Internet", "Oktoberfest de Blumenau",
]


def chamar_api(params: dict, tentativas: int = 5) -> dict:
    """Faz uma chamada GET à API do MediaWiki e devolve o JSON decodificado.

    Em HTTP 429 (limite de taxa), espera o tempo de Retry-After (ou um backoff
    crescente) e tenta de novo, até o número de tentativas.
    """
    url = API + "?" + urllib.parse.urlencode({**params, "format": "json", "formatversion": "2"})
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for tentativa in range(tentativas):
        try:
            with urllib.request.urlopen(req, timeout=30, context=CONTEXTO_SSL) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as erro:
            if erro.code != 429 or tentativa == tentativas - 1:
                raise
            espera = int(erro.headers.get("Retry-After") or 0) or 5 * (tentativa + 1)
            time.sleep(espera)


class ExtratorParagrafos(HTMLParser):
    """Extrai o texto de cada <p> do HTML renderizado, ignorando tabelas, infobox e notas."""

    def __init__(self):
        super().__init__()
        self.paragrafos: list[str] = []
        self._dentro_p = False
        self._ignorar = 0  # profundidade dentro de <sup>/<style>, cujo texto não interessa
        self._atual: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self._dentro_p, self._atual = True, []
        elif tag in ("sup", "style") and self._dentro_p:
            self._ignorar += 1

    def handle_endtag(self, tag):
        if tag in ("sup", "style") and self._ignorar:
            self._ignorar -= 1
        elif tag == "p" and self._dentro_p:
            texto = re.sub(r"\s+", " ", "".join(self._atual)).strip()
            # Parágrafos muito curtos costumam ser legendas ou restos de template
            if len(texto.split()) >= 15:
                self.paragrafos.append(texto)
            self._dentro_p = False

    def handle_data(self, data):
        if self._dentro_p and not self._ignorar:
            self._atual.append(data)


def slug(titulo: str) -> str:
    """Converte o título em nome de arquivo ASCII minúsculo com hífens."""
    s = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def baixar(titulo: str) -> str | None:
    """Baixa a revisão pré-corte de um artigo e grava o arquivo; devolve o caminho ou None."""
    dados = chamar_api({
        "action": "query", "prop": "revisions", "titles": titulo, "redirects": 1,
        "rvlimit": 1, "rvstart": CORTE, "rvdir": "older", "rvprop": "ids|timestamp",
    })
    pagina = dados["query"]["pages"][0]
    if "revisions" not in pagina:
        print(f"  sem revisão anterior ao corte: {titulo}")
        return None
    rev = pagina["revisions"][0]
    html = chamar_api({"action": "parse", "oldid": rev["revid"], "prop": "text"})["parse"]["text"]
    extrator = ExtratorParagrafos()
    extrator.feed(html)
    corpo = "\n\n".join(extrator.paragrafos)
    cabecalho = (
        f"<!-- fonte: Wikipédia, \"{pagina['title']}\", revisão {rev['revid']} de {rev['timestamp']}\n"
        f"     https://pt.wikipedia.org/w/index.php?oldid={rev['revid']}\n"
        f"     licença: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/) -->\n\n"
    )
    caminho = DESTINO / f"{slug(pagina['title'])}.md"
    caminho.write_text(cabecalho + corpo + "\n", encoding="utf-8")
    return f"{caminho.name} ({len(corpo.split())} palavras)"


if __name__ == "__main__":
    DESTINO.mkdir(parents=True, exist_ok=True)
    for titulo in ARTIGOS:
        # Reexecução não baixa de novo o que já existe (o slug do título pedido
        # pode diferir do título final após redirect, então isso é só um atalho)
        if (DESTINO / f"{slug(titulo)}.md").exists():
            continue
        try:
            resultado = baixar(titulo)
            if resultado:
                print(f"  ok: {resultado}")
        except Exception as erro:  # um artigo com problema não deve parar o lote
            print(f"  erro em {titulo}: {erro}")
        time.sleep(2)  # gentileza com a API, que limita clientes anônimos
