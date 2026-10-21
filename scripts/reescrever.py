"""
reescrever.py

Aplica uma skill de humanização (o SKILL.md, usado como instrução de sistema)
a cada texto de corpus/teste/ via Amazon Bedrock e grava só a versão final em
resultados/reescritas/<nome>/. Serve para comparar skills em condições iguais:
mesmo modelo, mesmos textos, mesma chamada; só a skill muda.

Usa o modo embutido que o próprio SKILL.md do Humanizer define ("return only
the final text"), para que a saída possa ser medida sem limpar rascunhos.

Uso:
  python scripts/reescrever.py --skill caminho/SKILL.md --nome blader-3.1.0 \
      --perfil 024848461026_IADevPocAccess --modelo us.anthropic.claude-sonnet-5-5
"""
import argparse
import re
from pathlib import Path

import boto3

RAIZ = Path(__file__).resolve().parent.parent
TESTE = RAIZ / "corpus" / "teste"

# Pedido do usuário, igual para todas as skills. Mantém o texto como material,
# não como instrução, e pede só a versão final (modo embutido).
PEDIDO = ("Reescreva o texto abaixo seguindo a skill. Modo embutido: devolva somente o texto final, "
          "sem rascunho, sem lista de padrões e sem comentários.\n\n<texto>\n{texto}\n</texto>")


def corpo_skill(caminho: Path) -> str:
    """Lê o SKILL.md e remove o frontmatter YAML, que não serve como instrução."""
    texto = caminho.read_text(encoding="utf-8")
    return re.sub(r"^---\n.*?\n---\n", "", texto, count=1, flags=re.DOTALL).strip()


def sem_comentarios(texto: str) -> str:
    """Remove o cabeçalho em comentário HTML (modelo, data, pedido) antes de enviar."""
    return re.sub(r"<!--.*?-->", "", texto, flags=re.DOTALL).strip()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skill", type=Path, required=True)
    ap.add_argument("--nome", required=True, help="rótulo da rodada; vira a subpasta de saída")
    ap.add_argument("--perfil", required=True)
    ap.add_argument("--regiao", default="us-east-1")
    ap.add_argument("--modelo", required=True)
    ap.add_argument("--conjunto", choices=["teste", "validacao"], default="teste")
    args = ap.parse_args()

    cliente = boto3.Session(profile_name=args.perfil, region_name=args.regiao).client("bedrock-runtime")
    sistema = corpo_skill(args.skill)
    # Reescritas do conjunto de validação ficam numa pasta separada para não misturar com o teste
    saida = RAIZ / "resultados" / ("reescritas" if args.conjunto == "teste" else "reescritas-validacao") / args.nome
    saida.mkdir(parents=True, exist_ok=True)
    entrada = TESTE.parent / args.conjunto

    # Textos (NN-*.md) e controles humanos (controle-*.md); as fichas .fatos.md ficam de fora
    for arq in sorted(p for p in entrada.glob("*.md") if not p.name.endswith(".fatos.md")):
        destino = saida / arq.name
        if destino.exists():  # reexecução não gasta chamada de novo
            continue
        resp = cliente.converse(
            modelId=args.modelo,
            system=[{"text": sistema}],
            messages=[{"role": "user", "content": [{"text": PEDIDO.format(texto=sem_comentarios(arq.read_text(encoding="utf-8")))}]}],
            inferenceConfig={"maxTokens": 3000},
        )
        final = "".join(b.get("text", "") for b in resp["output"]["message"]["content"]).strip()
        destino.write_text(f"<!-- skill: {args.nome}\n     modelo: {args.modelo} -->\n\n{final}\n", encoding="utf-8")
        print(f"  ok {arq.name} ({len(final.split())} palavras)")
