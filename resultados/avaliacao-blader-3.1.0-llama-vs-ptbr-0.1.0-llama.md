# Avaliação: A = `blader-3.1.0-llama` contra B = `ptbr-0.1.0-llama`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | B | 2.0 | 3.0 | 3/1 | 1/0 |
| 02-post-linkedin | empate | 3.5 | 3.5 | 1/0 | 2/0 |
| 03-post-linkedin | B | 2.5 | 4.0 | 2/0 | 0/0 |
| 04-relatorio | B | 3.5 | 4.5 | 0/0 | 1/0 |
| 05-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 06-relatorio | B | 3.0 | 4.5 | 0/0 | 0/0 |
| 07-email-cliente | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 08-email-cliente | B | 3.0 | 4.0 | 0/0 | 1/0 |
| 09-apresentacao | B | 2.0 | 3.5 | 0/0 | 0/0 |
| 10-apresentacao | B | 2.0 | 3.0 | 2/0 | 0/1 |
| 11-resposta-chat | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 12-resposta-chat | B | 2.5 | 3.5 | 1/0 | 0/0 |
| controle-embraer | B | 3.0 | 4.0 | 2/1 | 4/1 |
| controle-nubank | B | 3.0 | 4.0 | 3/1 | 3/1 |

**Resumo:** B venceu 13.5 de 14 (A 0.5). Naturalidade média A 2.79, B 3.82. Fatos perdidos A 14, B 12; inventados A 3, B 3.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": ["Havia muitos chamados chegando no cenário inicial.", "A solução não foi trocar o modelo.", "A solução não foi aumentar a complexidade da arquitetura."], "inventados": ["O tempo médio de 12 minutos era devido à priorização manual e às categorias variadas."]}; B {"perdidos": ["O modelo passou a entender melhor as diferenças entre categorias parecidas."], "inventados": []}

**02-post-linkedin**: A {"perdidos": ["As fichas do catálogo eram relativamente padronizadas."], "inventados": []}; B {"perdidos": ["A abordagem anterior tratava tudo como texto solto para embeddings.", "O original menciona que o domínio tinha entidades conhecidas."], "inventados": []}

**03-post-linkedin**: A {"perdidos": ["O estudo analisava a efetividade dos sistemas em contextos reais de interação com usuários.", "O professor Carlos Menezes também foi agradecido pelas contribuições ao longo do processo."], "inventados": []}; B {"perdidos": [], "inventados": []}

**04-relatorio**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["O aumento do volume de requisições ocorria especialmente em períodos de maior uso."], "inventados": []}

**08-email-cliente**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A tabela deve ser mantida atualizada mensalmente para garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}

**10-apresentacao**: A {"perdidos": ["A garrafa é indicada para café, chá, água, sucos e outras bebidas.", "A alça dobrável facilita também o armazenamento."], "inventados": []}; B {"perdidos": [], "inventados": ["A reescrita afirma que a tampa com trava evita vazamentos, enquanto o original diz apenas que ela ajuda a evitar vazamentos."]}

**12-resposta-chat**: A {"perdidos": ["Strands Agents é um SDK da AWS."], "inventados": []}; B {"perdidos": [], "inventados": []}

**controle-embraer**: A {"perdidos": ["A infraestrutura do aeroporto de São José dos Campos é mantida em parceria com a Infraero.", "A pista de Gavião Peixoto é identificada no original como o aeródromo de Gavião Peixoto."], "inventados": ["A reescrita afirma que a pista do aeroporto de São José dos Campos é compartilhada com a Infraero para uso comercial; no original, a infraestrutura é compartilhada e mantida em parceria com a Infraero, e a pista é usada pela Embraer e pelo transporte aéreo comercial."]}; B {"perdidos": ["A receita líquida de 2016 também correspondia a 6,1 bilhões de dólares.", "A área da pista/aeroporto de São José dos Campos pertence ao Departamento de Ciência e Tecnologia Aeroespacial.", "A pista/aeroporto de São José dos Campos é utilizada também para transporte aéreo comercial.", "Toda a infraestrutura do aeroporto de São José dos Campos é compartilhada e mantida em parceria com a Infraero."], "inventados": ["A reescrita afirma que a pista do aeroporto de São José dos Campos é compartilhada com a Infraero e o Departamento de Ciência e Tecnologia Aeroespacial; no original, a área pertence ao Departamento de Ciência e Tecnologia Aeroespacial e a infraestrutura é compartilhada e mantida em parceria com a Infraero."]}

**controle-nubank**: A {"perdidos": ["O Nubank tem operações no Brasil.", "O Nubank é sediado em São Paulo.", "A conta digital lançada em 2017 era anteriormente denominada NuConta e agora é chamada conta digital do Nubank."], "inventados": ["O Nubank foi fundado em São Paulo."]}; B {"perdidos": ["O Nubank atua como operadora de cartões de crédito e fintech com operações no Brasil.", "O Nubank é sediado em São Paulo.", "A conta digital do Nubank era anteriormente denominada NuConta."], "inventados": ["O Nubank foi fundado em São Paulo."]}

