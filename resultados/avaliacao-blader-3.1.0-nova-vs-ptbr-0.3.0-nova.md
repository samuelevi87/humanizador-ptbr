# Avaliação: A = `blader-3.1.0-nova` contra B = `ptbr-0.3.0-nova`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | A | 3.0 | 2.0 | 3/0 | 6/0 |
| 02-post-linkedin | B | 3.0 | 4.0 | 3/0 | 0/0 |
| 03-post-linkedin | B | 2.0 | 3.0 | 0/0 | 0/0 |
| 04-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 05-relatorio | B | 3.0 | 4.0 | 0/0 | 1/0 |
| 06-relatorio | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 07-email-cliente | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 08-email-cliente | B | 3.0 | 4.0 | 2/0 | 1/0 |
| 09-apresentacao | B | 1.5 | 3.0 | 0/0 | 0/0 |
| 10-apresentacao | A | 4.0 | 2.0 | 3/0 | 0/0 |
| 11-resposta-chat | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 12-resposta-chat | A | 4.0 | 3.0 | 0/0 | 0/0 |
| controle-embraer | B | 3.0 | 4.0 | 2/0 | 1/0 |
| controle-nubank | B | 2.5 | 3.5 | 3/0 | 2/1 |

**Resumo:** B venceu 10.0 de 14 (A 4.0). Naturalidade média A 3.00, B 3.39. Fatos perdidos A 16, B 11; inventados A 0, B 1.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": ["A solução não foi trocar o modelo nem aumentar a complexidade da arquitetura.", "Os exemplos reais de chamados de cobrança adicionados ao prompt incluíam suas classificações corretas.", "Apesar de funcionar bem em várias categorias, o modelo falhava em chamados de cobrança."], "inventados": []}; B {"perdidos": ["Havia muitos chamados chegando no cenário inicial.", "Os chamados eram de categorias diferentes.", "A priorização era manual.", "O modelo funcionava bem em várias categorias, apesar de errar em chamados de cobrança.", "Os exemplos reais de chamados de cobrança adicionados ao prompt incluíam suas classificações corretas.", "A melhoria também ajudou o modelo a entender as diferenças entre categorias parecidas."], "inventados": []}

**02-post-linkedin**: A {"perdidos": ["A abordagem anterior tratava tudo como texto solto para embeddings.", "O catálogo foi organizado como uma base mais estruturada com campos claros.", "O original menciona que o domínio tinha entidades conhecidas."], "inventados": []}; B {"perdidos": [], "inventados": []}

**05-relatorio**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A busca de todas as mensagens pelo ID da conversa é a consulta principal/mais comum do sistema."], "inventados": []}

**08-email-cliente**: A {"perdidos": ["O cliente perguntou se o agente pode responder sobre preços.", "A atualização mensal da planilha é necessária para garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}; B {"perdidos": ["A atualização mensal da planilha serve para garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}

**10-apresentacao**: A {"perdidos": ["É indicada para dia a dia, viagens, trabalho, academia ou passeios.", "A tampa com trava ajuda a evitar vazamentos.", "A alça dobrável facilita o armazenamento."], "inventados": []}; B {"perdidos": [], "inventados": []}

**controle-embraer**: A {"perdidos": ["Que, no aeroporto de São José dos Campos, toda a infraestrutura é compartilhada e mantida em parceria com a Infraero.", "Que a pista de Gavião Peixoto é identificada como o aeródromo de Gavião Peixoto."], "inventados": []}; B {"perdidos": ["A infraestrutura do aeroporto de São José dos Campos é mantida em parceria com a Infraero."], "inventados": []}

**controle-nubank**: A {"perdidos": ["O cartão de crédito lançado em 2014 tinha bandeira Mastercard.", "A conta digital do Nubank era anteriormente denominada NuConta.", "Em 2019, os empréstimos passaram a ser oferecidos para alguns clientes."], "inventados": []}; B {"perdidos": ["O Nubank foi fundado em 6 de maio de 2013.", "A conta digital do Nubank era anteriormente denominada NuConta."], "inventados": ["O Nubank iniciou suas operações em 6 de maio de 2013."]}

