# Análise v1 do catálogo

Corpus: 180 textos de IA (6 modelos × 30 pedidos, 67 mil palavras) contra 19 artigos da Wikipédia lusófona anteriores a 30/11/2022 (82 mil palavras). Tabelas completas em `frequencias-v1.md` e `ngramas-v1.md`.

## Faixas

Razão = ocorrências por mil palavras em IA ÷ no humano. "Só IA" = zero no humano.

**Fortes** (entram no SKILL.md com força de ação em uma ocorrência):

| Padrão | Razão | Observação |
|---|---|---|
| E26 placeholder de texto-modelo | 85,5 | `[Nome da Empresa]`, `[Valor]`, `[Porcentagem]`; vem da descoberta por n-gramas |
| C16 linguagem de vendas | 18,9 | puxado por Llama |
| C12 vocabulário típico de IA | 10,4 | lista PT refeita do zero |
| G11 finalidade genérica | 9,8 | "para garantir", "essencial para", "a importância de"; vem da descoberta |
| G6 substantivos de palestra | 7,9 | "jornada", "ecossistema", "pilares" |
| A1 não X, é Y | 5,9 | inclui forma dividida em duas frases |
| G5 verbos corporativos inflados | 5,1 | "alavancar", "potencializar", "impulsionar" |
| E22 resíduo de chatbot | só IA | "Se quiser, posso ajustar o tom", "Aqui está um rascunho" |
| C13 importância inflada | só IA | baixa frequência (0,31/mil), mas zero no humano |

**Médios** (contam com companhia de outro padrão no mesmo trecho):

| Padrão | Razão | Observação |
|---|---|---|
| C15 gerúndio em cascata | 4,0 | inclui "permitindo que" |
| C14 conexão vaga | 2,8 | |
| B8 travessão | 2,5 | depende muito do modelo: Mistral 4,7/mil, Claude 2,5, GPT 2,1; Llama e Nova zero |
| G1 conectores de redação | 2,4 | |
| B6 tríade | 2,2 | regex só pega tríade de substantivos no fim da frase |

**Descartados** (razão ≤ 1,3: humano usa igual ou mais):

B11 passiva analítica (0,8), G4 calques (1,0), G7 "realizar/efetuar" (1,3), G8 "possui" (0,6), G9 fórmulas formais (0,6), C18 "atua como/conta com" (0,4).

**Hipótese refutada:** G2 "vale ressaltar / é importante destacar" teve zero ocorrência nos 180 textos. Os modelos atuais parecem ter abandonado essa fórmula; fica fora do catálogo ou, no máximo, como nota histórica.

**Inconclusivos** (zero ou quase zero nos dois lados; o regex de frase literal é estreito demais): A2 fechos de efeito, A3 frase profunda, A5 discutir com ninguém, B9 qualificadores, G3 abertura de cenário, G10 pergunta retórica, E23 limite de conhecimento, E25 escrever sobre o documento. Os padrões estruturais do grupo A vêm do original e aparecem na leitura (ex.: `corpus/teste/01-post-linkedin.md`); entram no SKILL.md pela leitura, não pela contagem.

**Sem controle válido:** D19 negrito e D20 emoji. O extrator da Wikipédia remove a formatação, então "só IA" aqui é artefato.

## Ressalvas

1. **Um gênero só no controle humano.** A Wikipédia é enciclopédica: não tem segunda pessoa, e-mail nem post. N-gramas como "se você", "você pode" e "espero que" aparecem como "só IA" por gênero, não por estilo. Por isso não viraram padrão. Falta um controle humano de e-mail e post anterior a 2022.
2. **Os posts do autor no LinkedIn não servem de controle**: a maioria é de 2024 em diante e tem os mesmos padrões do corpus de IA.
3. **Amostra pequena por modelo** (cerca de 11 mil palavras cada): valores abaixo de 0,2/mil são uma ou duas ocorrências.
