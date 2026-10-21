# Avaliação: A = `blader-3.1.0` contra B = `ptbr-0.2.0`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 02-post-linkedin | empate | 4.0 | 4.0 | 0/0 | 0/0 |
| 03-post-linkedin | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 04-relatorio | A | 5.0 | 4.0 | 1/1 | 0/0 |
| 05-relatorio | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 06-relatorio | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 07-email-cliente | A | 5.0 | 4.0 | 0/1 | 0/0 |
| 08-email-cliente | B | 4.0 | 5.0 | 0/0 | 0/0 |
| 09-apresentacao | A | 5.0 | 4.0 | 0/0 | 0/0 |
| 10-apresentacao | B | 3.5 | 4.0 | 0/0 | 0/0 |
| 11-resposta-chat | A | 5.0 | 4.0 | 0/0 | 0/0 |
| 12-resposta-chat | A | 4.0 | 3.0 | 0/0 | 0/0 |
| controle-embraer | B | 3.5 | 4.5 | 0/0 | 1/0 |
| controle-nubank | B | 3.0 | 4.0 | 1/0 | 0/0 |

**Resumo:** B venceu 7.0 de 14 (A 7.0). Naturalidade média A 4.00, B 3.96. Fatos perdidos A 2, B 1; inventados A 2, B 0.

## Detalhe de fidelidade

**04-relatorio**: A {"perdidos": ["A recomendação original era manter o monitoramento para evitar novas ocorrências."], "inventados": ["A reescrita afirma que o monitoramento serve para detectar novas ocorrências."]}; B {"perdidos": [], "inventados": []}

**07-email-cliente**: A {"perdidos": [], "inventados": ["Pedido para o cliente indicar quem cuida da liberação do acesso."]}; B {"perdidos": [], "inventados": []}

**controle-embraer**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A Embraer nasceu no Brasil."], "inventados": []}

**controle-nubank**: A {"perdidos": ["O Nubank tem operações no Brasil."], "inventados": []}; B {"perdidos": [], "inventados": []}

