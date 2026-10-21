"""
contar_padroes.py

Mede a frequência de cada padrão de scripts/padroes.yaml por mil palavras em
dois conjuntos de texto (IA e humano) e calcula a razão entre eles. É a base
para decidir quais padrões entram no catálogo do SKILL.md: um padrão que
aparece igual nos dois lados geraria falso positivo e fica de fora.

Aceita diretórios (lidos recursivamente, *.md e *.txt). Comentários HTML, como
o cabeçalho de atribuição da Wikipédia, são removidos antes da contagem.

Uso:
  python scripts/contar_padroes.py corpus/ia corpus/humano
  python scripts/contar_padroes.py corpus/ia corpus/humano --por-pasta   # quebra por subpasta de IA (modelo)
  python scripts/contar_padroes.py corpus/ia corpus/humano --saida resultados/frequencias-v0.md
"""
import argparse
import re
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent


def carregar_padroes(caminho: Path) -> list[dict]:
    """Lê padroes.yaml e compila as regex de cada padrão."""
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    for p in dados["padroes"]:
        p["compiladas"] = [re.compile(rx, re.IGNORECASE | re.MULTILINE) for rx in p["regex"]]
    return dados["padroes"]


def ler_textos(pasta: Path) -> str:
    """Concatena o texto de todos os .md/.txt da pasta, sem comentários HTML."""
    partes = [p.read_text(encoding="utf-8") for p in sorted(pasta.rglob("*")) if p.suffix in {".md", ".txt"}]
    return re.sub(r"<!--.*?-->", "", "\n\n".join(partes), flags=re.DOTALL)


def taxas(texto: str, padroes: list[dict]) -> tuple[dict, int]:
    """Devolve ({id: ocorrências por mil palavras}, total de palavras)."""
    palavras = max(len(texto.split()), 1)  # evita divisão por zero em pasta vazia
    resultado = {}
    for p in padroes:
        n = sum(len(rx.findall(texto)) for rx in p["compiladas"])
        resultado[p["id"]] = n * 1000 / palavras
    return resultado, palavras


def razao(ia: float, humano: float) -> str:
    """Formata a razão ia/humano; 'só IA' quando o humano é zero e a IA não."""
    if humano == 0:
        return "só IA" if ia > 0 else "-"
    return f"{ia / humano:.1f}"


def tabela(padroes: list[dict], colunas: dict[str, dict], humano: dict) -> str:
    """Monta uma tabela Markdown com uma coluna por conjunto de IA, a coluna humana e a razão geral."""
    nomes = list(colunas)
    linhas = ["| Padrão | " + " | ".join(nomes) + " | humano | razão |",
              "|---" * (len(nomes) + 3) + "|"]
    geral = colunas[nomes[0]]  # a primeira coluna é sempre o conjunto completo de IA
    for p in padroes:
        valores = " | ".join(f"{colunas[n][p['id']]:.2f}" for n in nomes)
        linhas.append(f"| {p['id']} {p['nome']} | {valores} | {humano[p['id']]:.2f} | {razao(geral[p['id']], humano[p['id']])} |")
    return "\n".join(linhas)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ia", type=Path)
    ap.add_argument("humano", type=Path)
    ap.add_argument("--padroes", type=Path, default=RAIZ / "padroes.yaml")
    ap.add_argument("--por-pasta", action="store_true", help="adiciona uma coluna por subpasta do diretório de IA")
    ap.add_argument("--saida", type=Path, help="grava a tabela em Markdown neste arquivo")
    args = ap.parse_args()

    padroes = carregar_padroes(args.padroes)
    ia_geral, n_ia = taxas(ler_textos(args.ia), padroes)
    humano, n_hum = taxas(ler_textos(args.humano), padroes)

    colunas = {"IA (todos)": ia_geral}
    if args.por_pasta:
        for sub in sorted(d for d in args.ia.iterdir() if d.is_dir()):
            colunas[sub.name] = taxas(ler_textos(sub), padroes)[0]

    saida = (f"Ocorrências por mil palavras. IA: {n_ia} palavras; humano: {n_hum} palavras.\n\n"
             + tabela(padroes, colunas, humano) + "\n")
    print(saida)
    if args.saida:
        args.saida.parent.mkdir(parents=True, exist_ok=True)
        args.saida.write_text(saida, encoding="utf-8")
