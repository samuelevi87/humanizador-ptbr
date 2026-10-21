"""
checar_numeros.py

Checagem determinística de fidelidade: extrai cada número, porcentagem, valor
e data das fichas de fatos (NN.fatos.md) e verifica se aparece na reescrita.
Complementa o juiz LLM, que se mostrou ruidoso para fatos (marcou como
perdidos números que estavam no texto). Números são o fato mais importante
de preservar e o mais fácil de verificar sem modelo.

Normaliza grafias equivalentes antes de comparar: "6" e "seis", "1,2" e "1.2",
"30 mil" e "30.000", "R$ 149,90" e "149,90".

Uso:
  python scripts/checar_numeros.py ptbr-0.2.0-nova blader-3.1.0-nova [--conjunto validacao]
"""
import argparse
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Números por extenso que os modelos às vezes usam no lugar do algarismo
# ("um" e "uma" ficam de fora: na maioria das vezes são artigo, não número)
EXTENSO = {"dois": "2", "duas": "2", "três": "3", "quatro": "4", "cinco": "5",
           "seis": "6", "sete": "7", "oito": "8", "nove": "9", "dez": "10", "doze": "12", "quinze": "15", "vinte": "20"}
NUMERO = re.compile(r"\d+(?:[.,]\d+)*")


def normalizar(texto: str) -> str:
    """Põe o texto em forma comparável: minúsculas, extenso vira algarismo, '30 mil' vira '30000'."""
    t = texto.lower()
    # "um em cada cinco" é número, mesmo com "um" fora da tabela de extenso
    t = re.sub(r"(?<!\w)uma? em cada(?!\w)", "1 em cada", t)
    for palavra, digito in EXTENSO.items():
        t = re.sub(rf"(?<!\w){palavra}(?!\w)", digito, t)
    t = re.sub(r"(\d+)\s*mil(?!\w)", lambda m: m.group(1) + "000", t)
    t = re.sub(r"(?<=\d)\.(?=\d{3}(?!\d))", "", t)  # separador de milhar: 1.200 -> 1200
    return t.replace(",", ".")


def numeros(texto: str) -> set[str]:
    """Conjunto de números normalizados do texto."""
    return set(NUMERO.findall(normalizar(texto)))


def checar(rodada: str, conjunto: str) -> tuple[int, int, list[str]]:
    """Devolve (números esperados, números ausentes, detalhes) para uma rodada de reescrita."""
    base = RAIZ / "corpus" / conjunto
    pasta = RAIZ / "resultados" / ("reescritas" if conjunto == "teste" else "reescritas-validacao") / rodada
    esperados = ausentes = 0
    detalhes = []
    for ficha in sorted(base.glob("*.fatos.md")):
        # A pergunta do usuário nas respostas de chat não precisa reaparecer
        fatos = "\n".join(l for l in ficha.read_text(encoding="utf-8").splitlines() if "Pergunta do usuário" not in l)
        alvo = numeros(fatos)
        reescrita = (pasta / ficha.name.replace(".fatos.md", ".md")).read_text(encoding="utf-8")
        reescrita = re.sub(r"<!--.*?-->", "", reescrita, flags=re.DOTALL)
        faltam = sorted(alvo - numeros(reescrita))
        esperados += len(alvo)
        ausentes += len(faltam)
        if faltam:
            detalhes.append(f"{ficha.name.replace('.fatos.md', '')}: faltam {', '.join(faltam)}")
    return esperados, ausentes, detalhes


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rodadas", nargs="+")
    ap.add_argument("--conjunto", choices=["teste", "validacao"], default="teste")
    args = ap.parse_args()
    for rodada in args.rodadas:
        esperados, ausentes, detalhes = checar(rodada, args.conjunto)
        print(f"{rodada}: {esperados - ausentes}/{esperados} números preservados")
        for d in detalhes:
            print(f"   {d}")
