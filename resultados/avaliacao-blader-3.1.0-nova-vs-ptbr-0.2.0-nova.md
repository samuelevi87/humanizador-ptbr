# Avaliação: A = `blader-3.1.0-nova` contra B = `ptbr-0.2.0-nova`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | empate | 2.5 | 2.5 | 4/0 | 5/1 |
| 02-post-linkedin | A | 4.0 | 2.5 | 0/0 | 0/0 |
| 03-post-linkedin | B | 2.0 | 3.5 | 0/0 | 0/0 |
| 04-relatorio | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 05-relatorio | B | 2.5 | 3.0 | 0/0 | 0/0 |
| 06-relatorio | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 07-email-cliente | empate | 3.0 | 3.0 | 0/0 | 0/0 |
| 08-email-cliente | empate | 3.5 | 3.5 | 1/0 | 1/0 |
| 09-apresentacao | empate | 1.5 | 2.0 | 0/0 | 0/0 |
| 10-apresentacao | A | 4.5 | 2.0 | 3/0 | 0/0 |
| 11-resposta-chat | A | 3.5 | 2.5 | 0/0 | 0/0 |
| 12-resposta-chat | A | 4.0 | 3.0 | 0/0 | 0/0 |
| controle-embraer | A | 4.0 | 2.5 | 2/0 | 3/1 |
| controle-nubank | A | 3.5 | 2.5 | 3/0 | 8/0 |

**Resumo:** B venceu 5.0 de 14 (A 9.0). Naturalidade média A 3.29, B 2.86. Fatos perdidos A 13, B 17; inventados A 0, B 2.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": ["Os exemplos reais de chamados de cobrança adicionados ao prompt incluíam suas classificações corretas.", "A solução não foi trocar o modelo.", "A solução também não foi aumentar a complexidade da arquitetura.", "Antes da correção, o modelo funcionava bem em várias categorias, mas falhava em chamados de cobrança, um tipo sensível para o negócio."], "inventados": []}; B {"perdidos": ["No cenário inicial havia categorias diferentes de chamados.", "No cenário inicial havia priorização manual.", "Os exemplos reais de chamados de cobrança adicionados ao prompt incluíam suas classificações corretas.", "Os exemplos ajudaram o modelo a distinguir diferenças entre categorias parecidas.", "A solução não envolveu aumentar a complexidade da arquitetura."], "inventados": ["A reescrita afirma que a solução não foi aumentar a complexidade do modelo, enquanto o original fala em não aumentar a complexidade da arquitetura."]}

**08-email-cliente**: A {"perdidos": ["A tabela deve ser mantida atualizada mensalmente para garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}; B {"perdidos": ["A tabela deve ser mantida atualizada mensalmente para garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}

**10-apresentacao**: A {"perdidos": ["A tampa com trava ajuda a evitar vazamentos.", "A alça dobrável facilita o armazenamento.", "É indicada para dia a dia, viagens, trabalho, academia e passeios."], "inventados": []}; B {"perdidos": [], "inventados": []}

**controle-embraer**: A {"perdidos": ["A infraestrutura do aeroporto de São José dos Campos é mantida em parceria com a Infraero.", "A pista de Gavião Peixoto é identificada no original como o aeródromo de Gavião Peixoto."], "inventados": []}; B {"perdidos": ["A área do aeroporto de São José dos Campos é utilizada tanto pela Embraer quanto para transporte aéreo comercial.", "Toda a infraestrutura do aeroporto de São José dos Campos é compartilhada e mantida em parceria com a Infraero.", "A unidade de Gavião Peixoto é identificada no original como o aeródromo de Gavião Peixoto."], "inventados": ["A reescrita afirma que a pista de São José dos Campos é compartilhada com a Infraero; no original, quem é compartilhada e mantida em parceria com a Infraero é a infraestrutura, enquanto a área é usada pela Embraer e pelo transporte aéreo comercial."]}

**controle-nubank**: A {"perdidos": ["O cartão de crédito internacional lançado em 2014 tinha a bandeira Mastercard.", "A conta digital do Nubank era anteriormente denominada NuConta.", "Em 2019, o Nubank passou a oferecer empréstimos para alguns clientes, não de forma genericamente especificada."], "inventados": []}; B {"perdidos": ["Atuava também como operadora de cartões de crédito.", "Tinha operações no Brasil.", "O cartão de crédito lançado em 2014 tinha bandeira Mastercard.", "O Nubank Rewards era um programa de benefícios.", "A conta digital do Nubank era anteriormente denominada NuConta.", "Os empréstimos lançados em 2019 eram oferecidos apenas para alguns clientes.", "Em 2018, ao atingir o status de unicórnio, o Nubank era a terceira empresa brasileira com essa marca até então.", "A empresa ultrapassou instituições tradicionais, como o Banco do Brasil."], "inventados": []}

