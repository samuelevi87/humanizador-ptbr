# Avaliação: A = `blader-3.1.0-nova` contra B = `ptbr-0.1.0-nova`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | B | 2.0 | 4.0 | 2/0 | 4/0 |
| 02-post-linkedin | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 03-post-linkedin | B | 2.0 | 3.5 | 0/0 | 0/0 |
| 04-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 05-relatorio | empate | 2.5 | 3.0 | 0/0 | 5/0 |
| 06-relatorio | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 07-email-cliente | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 08-email-cliente | empate | 3.5 | 3.5 | 1/0 | 1/0 |
| 09-apresentacao | B | 2.0 | 3.5 | 0/0 | 0/0 |
| 10-apresentacao | A | 4.5 | 2.0 | 3/0 | 0/1 |
| 11-resposta-chat | A | 3.5 | 2.5 | 0/0 | 0/0 |
| 12-resposta-chat | A | 4.0 | 2.5 | 0/0 | 0/0 |
| controle-embraer | empate | 3.5 | 3.5 | 1/0 | 2/1 |
| controle-nubank | B | 3.0 | 4.0 | 3/1 | 2/0 |

**Resumo:** B venceu 6.5 de 14 (A 7.5). Naturalidade média A 3.25, B 3.21. Fatos perdidos A 10, B 14; inventados A 1, B 2.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": ["A solução não foi trocar o modelo nem aumentar a complexidade da arquitetura.", "Apesar de funcionar bem em várias categorias, o modelo falhava em um tipo de chamado sensível para o negócio."], "inventados": []}; B {"perdidos": ["Na primeira versão, o modelo classificava errado 1 em cada 5 chamados relacionados a cobrança.", "A solução não foi trocar o modelo nem aumentar a complexidade da arquitetura.", "Os exemplos reais de chamados de cobrança adicionados ao prompt incluíam suas classificações corretas.", "Os exemplos ajudaram o modelo a entender melhor os padrões, a linguagem usada pelos clientes e as diferenças entre categorias parecidas."], "inventados": []}

**05-relatorio**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["O volume previsto é de aproximadamente 30 mil conversas por mês.", "A consulta principal do sistema é buscar todas as mensagens associadas a uma conversa a partir do ID da conversa.", "O DynamoDB permite escalar conforme o crescimento do volume de conversas.", "O PostgreSQL foi considerado uma solução relacional madura e flexível.", "O caso de uso atual não exige joins ou transações complexas."], "inventados": []}

**08-email-cliente**: A {"perdidos": ["A atualização mensal da planilha é necessária para garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}; B {"perdidos": ["A atualização mensal da tabela tem como objetivo garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}

**10-apresentacao**: A {"perdidos": ["Perfeita para o dia a dia, viagens, trabalho, academia ou passeios.", "A tampa com trava ajuda a evitar vazamentos.", "A alça dobrável facilita o transporte e o armazenamento."], "inventados": []}; B {"perdidos": [], "inventados": ["A tampa com trava de segurança evita vazamentos de forma categórica; no original, ela apenas ajuda a evitar vazamentos."]}

**controle-embraer**: A {"perdidos": ["No aeroporto de São José dos Campos, toda a infraestrutura é mantida em parceria com a Infraero."], "inventados": []}; B {"perdidos": ["No aeroporto de São José dos Campos, toda a infraestrutura é mantida em parceria com a Infraero.", "A unidade de Gavião Peixoto é o aeródromo de Gavião Peixoto."], "inventados": ["A pista/área de São José dos Campos é compartilhada com a Infraero para transporte aéreo comercial."]}

**controle-nubank**: A {"perdidos": ["O cartão de crédito internacional lançado em 2014 tinha bandeira Mastercard.", "A conta digital do Nubank era anteriormente denominada NuConta.", "Em 2019, o Nubank passou a oferecer empréstimos para alguns clientes, não necessariamente para todos."], "inventados": ["O Nubank opera como emissora de cartões de crédito."]}; B {"perdidos": ["O Nubank tem operações no Brasil.", "A conta digital do Nubank era anteriormente denominada NuConta."], "inventados": []}

