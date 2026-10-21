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

## 0.2.0

- Bloco "Regras que não podem falhar" no topo: todo dado fica, nada novo entra, a forma continua, o catálogo precisa ser aplicado de verdade.
- Resultado: corrigiu a perda de números com Nova, mas fez o Claude conservar frases demais (saídas 12% mais longas) e piorou a preferência.

## 0.3.0

- Regra 1 reescrita como "todo dado fica, a frase não": preservar o dado não é preservar a frase, e a versão final mais curta é o normal.
- Verificador determinístico de números (`checar_numeros.py`) no lugar do juiz LLM para fatos numéricos; medição de ruído do juiz (estável entre rodadas).
- Conjunto de validação separado, nunca usado para ajustar a skill.

## 1.0.0

- Publicação da 0.3.0 como versão estável, com README de resultados e workflow de validação (`validar_pacote.py`).
- Validação: preferida pelo juiz em 10,5/14 (Claude), 11/14 (Llama) e 7,5/14 (Nova, com 18 fatos perdidos contra 47 do original); 35/35 números preservados nos três.
- Teste cego humano: mais humana em 3 de 6 textos e nunca a pior.
- Limites conhecidos e próximos ajustes: manter parágrafos curtos em post, não formalizar o que já é natural, edição mínima em texto sem padrões fortes.
