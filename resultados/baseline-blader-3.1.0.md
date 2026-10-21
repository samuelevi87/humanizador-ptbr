# Linha de base: Humanizer original (blader 3.1.0) em português

Mesmo `SKILL.md` (v3.1.0, instalado do marketplace) como instrução de sistema, em modo embutido, aplicado aos 12 textos de `corpus/teste/` e a 2 controles humanos (trechos da Wikipédia pré-2022), com três modelos reescritores via Bedrock. Reescritas em `reescritas/blader-3.1.0*/`.

## Resultado por modelo reescritor

**Claude Sonnet 5.5** (`reescritas/blader-3.1.0/`): reescrita quase sempre boa em português. Removeu contrastes "não foi X. Foi Y", fechos de uma linha, listas com ✅, resíduo de chat ("Ficamos à disposição") e o enchimento de apresentação institucional (texto 09: de 148 para 41 palavras, os 5 fatos preservados). Nos controles humanos, nenhum falso positivo relevante: não "corrigiu" sujeito oculto, trocou "possui" por "tem" e cortou o único floreio. Sobra isolada: "ecossistema AWS" no texto 12.

**Amazon Nova Pro** (`reescritas/blader-3.1.0-nova/`): falha visível. Juntou o post 01 em um parágrafo só e manteve "drasticamente", a lista de lições em sequência e o fecho "O maior ganho foi mostrar que...".

**Llama 4 Maverick** (`reescritas/blader-3.1.0-llama/`): falha visível. No texto 09 manteve quase todo o enchimento ("dedicação, qualidade e compromisso", "visão voltada para o futuro", "contribuindo para o desenvolvimento da indústria têxtil brasileira").

## O que isso muda

1. **A hipótese do plano não se sustenta para modelos de fronteira.** Os falsos positivos previstos para português (§10 hífen, §11 sujeito oculto) não apareceram com Claude Sonnet 5.5, e os tiques do português foram removidos mesmo sem catálogo em português: o modelo generaliza a partir dos exemplos em inglês.
2. **A hipótese se sustenta para modelos menores.** Com Nova Pro e Llama 4 o mesmo `SKILL.md` rende pouco em português. Um catálogo explícito em português, com exemplos em português, tende a ajudar justamente onde o modelo não generaliza sozinho.
3. **O contador por regex não serve como juiz das reescritas.** Ele não registra tríades no meio da frase nem enchimento institucional, que foram as falhas mais visíveis. A avaliação precisa do juiz LLM cego e da conferência de fatos (Fase 6).
