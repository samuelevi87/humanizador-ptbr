# Avaliação: A = `blader-3.1.0` contra B = `ptbr-0.1.0`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | A | 4.0 | 3.0 | 0/1 | 0/0 |
| 02-post-linkedin | empate | 4.0 | 3.5 | 0/0 | 0/0 |
| 03-post-linkedin | B | 3.0 | 4.0 | 1/0 | 0/0 |
| 04-relatorio | empate | 4.5 | 4.5 | 1/1 | 0/0 |
| 05-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 06-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 07-email-cliente | A | 4.5 | 3.5 | 0/1 | 0/0 |
| 08-email-cliente | B | 4.0 | 5.0 | 0/0 | 0/1 |
| 09-apresentacao | B | 4.0 | 5.0 | 0/0 | 0/0 |
| 10-apresentacao | B | 3.0 | 4.0 | 0/0 | 1/0 |
| 11-resposta-chat | B | 4.0 | 4.5 | 0/0 | 0/0 |
| 12-resposta-chat | B | 3.5 | 4.5 | 0/0 | 0/0 |
| controle-embraer | empate | 3.5 | 3.5 | 0/0 | 2/0 |
| controle-nubank | A | 4.0 | 3.0 | 1/0 | 0/0 |

**Resumo:** B venceu 9.5 de 14 (A 4.5). Naturalidade média A 3.71, B 4.00. Fatos perdidos A 3, B 3; inventados A 3, B 1.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": [], "inventados": ["Antes, a triagem era manual."]}; B {"perdidos": [], "inventados": []}

**03-post-linkedin**: A {"perdidos": ["O agradecimento ao professor Carlos Menezes também menciona suas contribuições ao longo do processo."], "inventados": []}; B {"perdidos": [], "inventados": []}

**04-relatorio**: A {"perdidos": ["A recomendação original era manter o monitoramento para evitar novas ocorrências."], "inventados": ["A reescrita afirma que o monitoramento deve continuar para detectar novas ocorrências."]}; B {"perdidos": [], "inventados": []}

**07-email-cliente**: A {"perdidos": [], "inventados": ["Pedido para que o cliente indique quem cuida da liberação do acesso."]}; B {"perdidos": [], "inventados": []}

**08-email-cliente**: A {"perdidos": [], "inventados": []}; B {"perdidos": [], "inventados": ["O alinhamento do formato da planilha e dos próximos passos pode ser feito \"por aqui mesmo\"."]}

**10-apresentacao**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A garrafa é indicada para o dia a dia, viagens, trabalho, academia ou passeios."], "inventados": []}

**controle-embraer**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A Embraer nasceu no Brasil.", "As unidades industriais, escritórios e centros de distribuição foram estabelecidos para atender demandas globais."], "inventados": []}

**controle-nubank**: A {"perdidos": ["O Nubank tem operações no Brasil."], "inventados": []}; B {"perdidos": [], "inventados": []}

