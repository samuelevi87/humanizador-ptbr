# Avaliação: A = `blader-3.1.0-llama` contra B = `ptbr-0.2.0-llama`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | A | 3.0 | 2.0 | 2/0 | 1/0 |
| 02-post-linkedin | B | 3.0 | 4.0 | 1/0 | 0/0 |
| 03-post-linkedin | B | 2.0 | 4.0 | 2/0 | 1/0 |
| 04-relatorio | B | 3.5 | 4.5 | 0/0 | 1/0 |
| 05-relatorio | B | 3.0 | 4.0 | 0/0 | 2/0 |
| 06-relatorio | B | 3.5 | 4.5 | 1/0 | 0/0 |
| 07-email-cliente | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 08-email-cliente | B | 3.0 | 4.5 | 1/0 | 2/0 |
| 09-apresentacao | B | 2.0 | 3.5 | 0/0 | 0/0 |
| 10-apresentacao | B | 2.0 | 3.0 | 2/0 | 0/0 |
| 11-resposta-chat | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 12-resposta-chat | empate | 2.5 | 2.5 | 1/0 | 0/0 |
| controle-embraer | B | 3.0 | 4.0 | 0/0 | 3/1 |
| controle-nubank | B | 3.0 | 4.0 | 3/1 | 3/1 |

**Resumo:** B venceu 12.5 de 14 (A 1.5). Naturalidade média A 2.82, B 3.75. Fatos perdidos A 13, B 13; inventados A 1, B 2.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": ["Havia muitos chamados chegando no cenário inicial.", "A solução não foi trocar o modelo nem aumentar a complexidade da arquitetura."], "inventados": []}; B {"perdidos": ["A solução não foi trocar o modelo nem aumentar a complexidade da arquitetura."], "inventados": []}

**02-post-linkedin**: A {"perdidos": ["O original menciona que as fichas eram relativamente padronizadas como uma condição em que a modelagem do catálogo pode superar a busca semântica genérica."], "inventados": []}; B {"perdidos": [], "inventados": []}

**03-post-linkedin**: A {"perdidos": ["O estudo considerava contextos reais de interação com usuários.", "O professor Carlos Menezes também fez contribuições ao longo do processo."], "inventados": []}; B {"perdidos": ["As contribuições do professor Carlos Menezes ao longo do processo."], "inventados": []}

**04-relatorio**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["O aumento do volume de requisições ocorria especialmente em períodos de maior uso."], "inventados": []}

**05-relatorio**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["O DynamoDB não é ideal para agregações flexíveis.", "A dificuldade de relatórios analíticos é diretamente sobre os dados operacionais."], "inventados": []}

**06-relatorio**: A {"perdidos": ["A correção do prompt também busca melhorar a consistência das respostas sobre prazo de entrega."], "inventados": []}; B {"perdidos": [], "inventados": []}

**08-email-cliente**: A {"perdidos": ["O cliente perguntou se o agente pode responder sobre preços."], "inventados": []}; B {"perdidos": ["A mensagem original responde afirmativamente a uma pergunta anterior do cliente, indicada por “Sim”.", "A atualização mensal da planilha serve para garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}

**10-apresentacao**: A {"perdidos": ["A alça dobrável facilita também o armazenamento.", "É ideal para café, chá, água, sucos e outras bebidas."], "inventados": []}; B {"perdidos": [], "inventados": []}

**12-resposta-chat**: A {"perdidos": ["Strands Agents é um SDK da AWS."], "inventados": []}; B {"perdidos": [], "inventados": []}

**controle-embraer**: A {}; B {"perdidos": ["A área do aeroporto de São José dos Campos pertence ao Departamento de Ciência e Tecnologia Aeroespacial.", "No aeroporto de São José dos Campos, toda a infraestrutura é mantida em parceria com a Infraero.", "A pista de Gavião Peixoto é identificada no original como o aeródromo de Gavião Peixoto."], "inventados": ["A reescrita afirma que a pista do aeroporto de São José dos Campos é compartilhada com a Infraero; no original, a infraestrutura é compartilhada e mantida em parceria com a Infraero, e o uso compartilhado mencionado é entre a Embraer e o transporte aéreo comercial."]}

**controle-nubank**: A {"perdidos": ["A empresa tem operações no Brasil.", "A empresa é sediada em São Paulo.", "A conta digital lançada em 2017 era anteriormente denominada NuConta e agora é chamada conta digital do Nubank."], "inventados": ["A empresa foi fundada em São Paulo."]}; B {"perdidos": ["O Nubank é sediado em São Paulo.", "O Nubank atua como operadora de cartões de crédito e fintech com operações no Brasil.", "A conta digital do Nubank era anteriormente denominada NuConta."], "inventados": ["O Nubank foi fundado em São Paulo."]}

