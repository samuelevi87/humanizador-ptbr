# Changelog

## 0.0.1

- Estrutura inicial do repositório, licença MIT com crédito ao Humanizer original.
- Corpus humano de controle: 19 artigos da Wikipédia lusófona na última revisão anterior a 30/11/2022.

## 0.0.2

- Corpus de IA ampliado para 180 textos (6 modelos × 30 pedidos via Bedrock) e corpus de teste com 12 textos e fichas de fatos.
- Descoberta de padrões por n-gramas com filtro por pedido; novos padrões E26 (placeholder) e G11 (finalidade genérica), resíduos de chat ampliados.
- Análise v1 com faixas forte, médio, descartado e inconclusivo em `resultados/analise-v1.md`.

## 0.1.0

- Primeira versão do SKILL.md em português: 27 padrões em sete grupos (A, B, P, C, D, E, F), com o grupo P medido em corpus e exemplos em português fora do conjunto de teste.
- Regras para modelos menores: preservar parágrafos, checklist final, placeholder nunca preenchido com valor inventado.
- Scripts reescrever.py (aplica uma skill via Bedrock em modo embutido) e avaliar.py (juiz cego de outra família, fidelidade e preferência nas duas ordens).
- Linha de base do Humanizer original com Claude, Nova e Llama.
