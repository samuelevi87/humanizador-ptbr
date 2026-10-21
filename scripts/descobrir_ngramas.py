"""
descobrir_ngramas.py

Descobre candidatos a padrão sem depender de lista prévia: compara a frequência
de sequências de 2 a 4 palavras (n-gramas) no corpus de IA e no corpus humano
e lista as que aparecem bem mais em texto de IA.

Para não confundir assunto com estilo (um n-grama como "computação em nuvem"
é frequente só porque o tema foi pedido), um n-grama só entra se aparecer em
vários pedidos diferentes (o nome do arquivo, ex. "relatorio-01", identifica o
pedido, que é o mesmo para todos os modelos) e em vários modelos. Assunto fica
preso ao pedido; hábito de escrita atravessa pedidos.

Uso:
  python scripts/descobrir_ngramas.py corpus/ia corpus/humano --saida resultados/ngramas-v0.md
"""
import argparse
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

PALAVRA = re.compile(r"[a-záàâãéêíóôõúüç]+(?:-[a-záàâãéêíóôõúüç]+)*", re.IGNORECASE)


def tokens(caminho: Path) -> list[str]:
    """Lê o arquivo, remove comentários HTML e Markdown de formatação e devolve as palavras em minúsculas."""
    texto = re.sub(r"<!--.*?-->", "", caminho.read_text(encoding="utf-8"), flags=re.DOTALL)
    return [t.lower() for t in PALAVRA.findall(texto)]


def ngramas(palavras: list[str], n: int) -> list[str]:
    """Devolve todos os n-gramas contíguos da lista de palavras."""
    return [" ".join(palavras[i:i + n]) for i in range(len(palavras) - n + 1)]


def contar(pasta: Path, ns: range) -> tuple[Counter, int, dict, dict]:
    """Conta n-gramas na pasta.

    Devolve (contagem total, total de palavras, pedidos em que cada n-grama
    aparece (nome do arquivo sem extensão), subpastas de primeiro nível
    (modelos) em que aparece).
    """
    total, n_palavras = Counter(), 0
    pedidos, modelos = defaultdict(set), defaultdict(set)
    for arq in sorted(pasta.rglob("*.md")):
        palavras = tokens(arq)
        n_palavras += len(palavras)
        modelo = arq.relative_to(pasta).parts[0]
        for n in ns:
            for g in ngramas(palavras, n):
                total[g] += 1
                pedidos[g].add(arq.stem)
                modelos[g].add(modelo)
    return total, n_palavras, pedidos, modelos


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ia", type=Path)
    ap.add_argument("humano", type=Path)
    ap.add_argument("--min-pedidos", type=int, default=5, help="mínimo de pedidos diferentes (de 10) em que o n-grama aparece")
    ap.add_argument("--min-modelos", type=int, default=3, help="mínimo de modelos diferentes em que aparece")
    ap.add_argument("--top", type=int, default=80)
    ap.add_argument("--saida", type=Path)
    args = ap.parse_args()

    ns = range(2, 5)
    ia, n_ia, arq_ia, mod_ia = contar(args.ia, ns)
    hum, n_hum, _, _ = contar(args.humano, ns)

    linhas = []
    for g, c in ia.items():
        if len(arq_ia[g]) < args.min_pedidos or len(mod_ia[g]) < args.min_modelos:
            continue
        # Razão de taxas por mil palavras com suavização de +0,5 para não dividir por zero
        taxa_ia = (c + 0.5) * 1000 / n_ia
        taxa_hum = (hum[g] + 0.5) * 1000 / n_hum
        linhas.append((math.log2(taxa_ia / taxa_hum), g, c, hum[g], len(arq_ia[g]), len(mod_ia[g])))

    linhas.sort(reverse=True)
    # Remove n-gramas contidos num n-grama maior já listado com contagem igual (evita repetição)
    escolhidos = []
    for linha in linhas:
        if not any(linha[1] in e[1] and linha[2] == e[2] for e in escolhidos):
            escolhidos.append(linha)
        if len(escolhidos) >= args.top:
            break

    saida = [f"N-gramas mais característicos de IA. IA: {n_ia} palavras; humano: {n_hum} palavras.",
             f"Filtro: aparece em ≥ {args.min_pedidos} pedidos e ≥ {args.min_modelos} modelos.\n",
             "| n-grama | log2 razão | IA | humano | pedidos | modelos |", "|---|---|---|---|---|---|"]
    saida += [f"| {g} | {lr:.1f} | {c} | {h} | {a} | {m} |" for lr, g, c, h, a, m in escolhidos]
    texto = "\n".join(saida) + "\n"
    print(texto)
    if args.saida:
        args.saida.write_text(texto, encoding="utf-8")
