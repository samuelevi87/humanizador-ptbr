# Teste cego humano: v0.3.0

Um avaliador (o autor do projeto, falante nativo) recebeu 6 textos do conjunto de validação, cada um em três versões embaralhadas (texto de IA sem revisão, Humanizer original 3.1.0 e humanizador-ptbr 0.3.0), e marcou a mais humana e a pior, sem saber a origem. Seleção com 2 textos por reescritor, incluindo casos em que o juiz LLM tinha preferido o Humanizer.

| Texto | Reescritor | Mais humana | Pior | Juiz LLM preferiu |
|---|---|---|---|---|
| 01 post (ponto eletrônico) | Claude | original de IA | Humanizer | PT-BR |
| 07 apresentação (parque) | Claude | PT-BR | original | Humanizer |
| 03 relatório (Black Friday) | Nova | PT-BR | Humanizer | PT-BR |
| 06 e-mail (desconto) | Nova | original de IA | Humanizer | Humanizer |
| 02 post (aulas em dupla) | Llama | Humanizer | original | PT-BR |
| 10 resposta (banco vetorial) | Llama | PT-BR | original | Humanizer |

**Contagem.** Mais humana: PT-BR 3, original de IA 2, Humanizer 1. Pior: Humanizer 3, original 3, PT-BR 0.

**Concordância com o juiz LLM.** O juiz só compara Humanizer e PT-BR, então a comparação vale nos 4 textos em que o humano escolheu uma das duas reescritas (02, 03, 05 e 07 da tabela: apresentação, relatório, post do Llama e resposta). Concordaram em 1 de 4 (o relatório 03). Nos dois textos restantes o humano preferiu o original, opção que o juiz nem avalia. Com essa concordância, o juiz LLM serve para comparar versões em escala e detectar regressão, não para dizer qual texto um leitor brasileiro prefere.

## Leitura dos casos em que o original venceu

- **Post 01:** o original tinha tiques ("Mais do que trocar uma ferramenta, implantamos um novo hábito", "E, no fim, esse foi o maior ganho"), mas tinha o ritmo de post: parágrafos curtos, com respiro. A PT-BR tirou os tiques e compactou o post em 4 parágrafos densos, com cara de relatório. Para post de rede social, a forma em parágrafos curtos é norma do gênero, não tique.
- **E-mail 06:** o original já estava natural. A PT-BR mexeu pouco e para pior: "Obrigado pelo seu contato" virou "Agradecemos seu interesse", mais formal sem motivo.

## Ajustes indicados

1. Post de rede social mantém parágrafos curtos e o respiro entre eles; o que sai é o fecho repetido e o contraste encenado, não a quebra de linha.
2. Não formalizar o que já é natural ("Obrigado" fica "Obrigado").
3. Texto sem padrões fortes pede edição mínima.
