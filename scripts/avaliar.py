"""
avaliar.py

Compara duas rodadas de reescrita (ex.: blader-3.1.0-nova contra ptbr-0.1.0-nova)
nos mesmos textos de corpus/teste/, com um modelo juiz de outra família via
Amazon Bedrock. Para cada texto faz dois julgamentos:

1. Fidelidade (para cada rodada, separadamente): o juiz recebe o original, a
   ficha de fatos (quando existe) e a reescrita, e lista fatos perdidos e
   afirmações inventadas.
2. Preferência cega: o juiz recebe as duas reescritas como "Texto 1" e
   "Texto 2", sem saber a origem, e diz qual soa mais como escrita humana em
   português do Brasil, com nota de naturalidade de 1 a 5 para cada. Roda nas
   duas ordens para anular o viés de posição.

Gera resultados/avaliacao-<A>-vs-<B>.md com a tabela por texto e o resumo.

Uso:
  python scripts/avaliar.py --a blader-3.1.0-nova --b ptbr-0.1.0-nova \
      --perfil 024848461026_IADevPocAccess --juiz us.openai.gpt-5.5
"""
import argparse
import json
import re
from pathlib import Path

import boto3

RAIZ = Path(__file__).resolve().parent.parent
TESTE = RAIZ / "corpus" / "teste"
REESCRITAS = RAIZ / "resultados" / "reescritas"

PROMPT_FIDELIDADE = """Você confere se uma reescrita preservou o conteúdo de um texto.

<original>
{original}
</original>
{fatos}
<reescrita>
{reescrita}
</reescrita>

Liste (1) os fatos concretos do original (números, nomes, datas, prazos, causas, decisões, pedidos) que NÃO aparecem na reescrita, e (2) as afirmações factuais da reescrita que NÃO estão no original. Cortar adjetivos, enchimento, opinião genérica ou frases de efeito NÃO conta como fato perdido. Reformular com outras palavras NÃO conta como invenção.

Responda só com JSON: {{"perdidos": ["..."], "inventados": ["..."]}}"""

PROMPT_PREFERENCIA = """Dois textos em português do Brasil dizem a mesma coisa. Avalie qual soa mais como escrito por uma pessoa, e não por um modelo de IA: sem frases de efeito, sem contraste "não é X, é Y", sem enchimento institucional, sem emojis decorativos, sem vocabulário de palestra, com português natural e não traduzido. Ignore diferenças de conteúdo.

<texto_1>
{t1}
</texto_1>

<texto_2>
{t2}
</texto_2>

Responda só com JSON: {{"mais_humano": 1 ou 2, "nota_1": 1-5, "nota_2": 1-5, "motivo": "uma frase"}}"""


def ler(caminho: Path) -> str:
    """Lê um arquivo do corpus sem o cabeçalho em comentário HTML."""
    return re.sub(r"<!--.*?-->", "", caminho.read_text(encoding="utf-8"), flags=re.DOTALL).strip()


def perguntar(cliente, juiz: str, prompt: str) -> dict:
    """Envia o prompt ao juiz e extrai o primeiro objeto JSON da resposta."""
    resp = cliente.converse(modelId=juiz, messages=[{"role": "user", "content": [{"text": prompt}]}],
                            inferenceConfig={"maxTokens": 1500})
    texto = "".join(b.get("text", "") for b in resp["output"]["message"]["content"])
    achado = re.search(r"\{.*\}", texto, re.DOTALL)
    return json.loads(achado.group(0)) if achado else {}


def fidelidade(cliente, juiz, original, fatos, reescrita) -> dict:
    """Pede ao juiz os fatos perdidos e as afirmações inventadas de uma reescrita."""
    bloco_fatos = f"\n<fatos_obrigatorios>\n{fatos}\n</fatos_obrigatorios>\n" if fatos else ""
    return perguntar(cliente, juiz, PROMPT_FIDELIDADE.format(original=original, fatos=bloco_fatos, reescrita=reescrita))


def preferencia(cliente, juiz, texto_a, texto_b) -> tuple[float, float, float]:
    """Roda a preferência nas duas ordens e devolve (pontos de A, nota média A, nota média B).

    Pontos de A: 1 se A venceu nas duas ordens, 0,5 se dividiu, 0 se perdeu nas duas.
    """
    r1 = perguntar(cliente, juiz, PROMPT_PREFERENCIA.format(t1=texto_a, t2=texto_b))
    r2 = perguntar(cliente, juiz, PROMPT_PREFERENCIA.format(t1=texto_b, t2=texto_a))
    pontos_a = (r1.get("mais_humano") == 1) * 0.5 + (r2.get("mais_humano") == 2) * 0.5
    nota_a = (r1.get("nota_1", 0) + r2.get("nota_2", 0)) / 2
    nota_b = (r1.get("nota_2", 0) + r2.get("nota_1", 0)) / 2
    return pontos_a, nota_a, nota_b


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--a", required=True, help="rodada A (subpasta de resultados/reescritas)")
    ap.add_argument("--b", required=True, help="rodada B")
    ap.add_argument("--perfil", required=True)
    ap.add_argument("--regiao", default="us-east-1")
    ap.add_argument("--juiz", required=True, help="modelId do juiz, de família diferente dos reescritores")
    ap.add_argument("--conjunto", choices=["teste", "validacao"], default="teste")
    args = ap.parse_args()
    if args.conjunto == "validacao":
        # Validação lê de outra pasta de textos e de reescritas, e grava com sufixo próprio
        TESTE = TESTE.parent / "validacao"
        REESCRITAS = REESCRITAS.parent / "reescritas-validacao"

    cliente = boto3.Session(profile_name=args.perfil, region_name=args.regiao).client("bedrock-runtime")
    linhas, soma = [], {"pontos_a": 0.0, "nota_a": 0.0, "nota_b": 0.0, "perd_a": 0, "inv_a": 0, "perd_b": 0, "inv_b": 0}
    detalhes = []

    arquivos = sorted(p for p in TESTE.glob("*.md") if not p.name.endswith(".fatos.md"))
    for arq in arquivos:
        original = ler(arq)
        ficha = arq.with_name(arq.stem + ".fatos.md")
        fatos = ler(ficha) if ficha.exists() else ""
        texto_a, texto_b = ler(REESCRITAS / args.a / arq.name), ler(REESCRITAS / args.b / arq.name)

        fid_a = fidelidade(cliente, args.juiz, original, fatos, texto_a)
        fid_b = fidelidade(cliente, args.juiz, original, fatos, texto_b)
        pontos_a, nota_a, nota_b = preferencia(cliente, args.juiz, texto_a, texto_b)

        pa, ia_ = len(fid_a.get("perdidos", [])), len(fid_a.get("inventados", []))
        pb, ib = len(fid_b.get("perdidos", [])), len(fid_b.get("inventados", []))
        for k, v in (("pontos_a", pontos_a), ("nota_a", nota_a), ("nota_b", nota_b), ("perd_a", pa), ("inv_a", ia_), ("perd_b", pb), ("inv_b", ib)):
            soma[k] += v
        vencedor = "A" if pontos_a == 1 else "B" if pontos_a == 0 else "empate"
        linhas.append(f"| {arq.stem} | {vencedor} | {nota_a:.1f} | {nota_b:.1f} | {pa}/{ia_} | {pb}/{ib} |")
        detalhes.append((arq.stem, fid_a, fid_b))
        print(f"  {arq.stem}: {vencedor} (A {nota_a:.1f}, B {nota_b:.1f}; fatos A {pa}/{ia_}, B {pb}/{ib})")

    n = len(arquivos)
    resumo = (f"# Avaliação: A = `{args.a}` contra B = `{args.b}`\n\nJuiz: `{args.juiz}`. Preferência cega nas duas ordens.\n\n"
              f"| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |\n|---|---|---|---|---|---|\n"
              + "\n".join(linhas)
              + f"\n\n**Resumo:** B venceu {n - soma['pontos_a']:.1f} de {n} (A {soma['pontos_a']:.1f}). "
              f"Naturalidade média A {soma['nota_a'] / n:.2f}, B {soma['nota_b'] / n:.2f}. "
              f"Fatos perdidos A {soma['perd_a']}, B {soma['perd_b']}; inventados A {soma['inv_a']}, B {soma['inv_b']}.\n\n## Detalhe de fidelidade\n\n")
    for nome, fa, fb in detalhes:
        if fa.get("perdidos") or fa.get("inventados") or fb.get("perdidos") or fb.get("inventados"):
            resumo += f"**{nome}**: A {json.dumps(fa, ensure_ascii=False)}; B {json.dumps(fb, ensure_ascii=False)}\n\n"
    sufixo = "" if args.conjunto == "teste" else "-validacao"
    destino = RAIZ / "resultados" / f"avaliacao{sufixo}-{args.a}-vs-{args.b}.md"
    destino.write_text(resumo, encoding="utf-8")
    print(f"\nResumo gravado em {destino.relative_to(RAIZ)}")
