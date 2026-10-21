"""
validar_pacote.py

Confere se o pacote está consistente antes de publicar: frontmatter do
SKILL.md válido, manifests JSON válidos, a mesma versão em SKILL.md,
plugin.json e no topo do CHANGELOG, e nenhum travessão usado como pausa na
prosa da skill (regra que a própria skill aplica).

Uso: python scripts/validar_pacote.py   (sai com código 1 se algo falhar)
"""
import json
import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent


def main() -> int:
    """Roda as checagens e devolve 0 se tudo passou, 1 se algo falhou."""
    erros = []
    skill = (RAIZ / "SKILL.md").read_text(encoding="utf-8")
    achado = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not achado:
        return print("SKILL.md sem frontmatter") or 1
    meta = yaml.safe_load(achado.group(1))
    for campo in ("name", "description", "license"):
        if not meta.get(campo):
            erros.append(f"SKILL.md sem o campo {campo}")
    versao_skill = str(meta.get("metadata", {}).get("version", ""))

    for nome in ("plugin.json", "marketplace.json"):
        try:
            json.loads((RAIZ / ".claude-plugin" / nome).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as erro:
            erros.append(f"{nome} inválido: {erro}")
    versao_plugin = json.loads((RAIZ / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")).get("version")

    # A versão mais recente do CHANGELOG é o primeiro título "## X.Y.Z" encontrado depois do topo
    versoes_changelog = re.findall(r"^## (\d+\.\d+\.\d+)", (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8"), re.MULTILINE)
    mais_recente = max(versoes_changelog, key=lambda v: tuple(map(int, v.split("."))), default="")
    if not (versao_skill == versao_plugin == mais_recente):
        erros.append(f"versões divergentes: SKILL.md {versao_skill}, plugin.json {versao_plugin}, CHANGELOG {mais_recente}")

    # Travessão como pausa na prosa: ignora linhas de exemplo (citação) e a linha da própria regra
    for n, linha in enumerate(skill.splitlines(), 1):
        if " — " in linha and not linha.startswith(">") and "**Regra:**" not in linha:
            erros.append(f"SKILL.md:{n} usa travessão como pausa")

    for e in erros:
        print(f"ERRO: {e}")
    print("ok" if not erros else f"{len(erros)} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
