# Avaliação: A = `blader-3.1.0` contra B = `ptbr-0.2.0`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 02-post-linkedin | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 03-post-linkedin | B | 3.0 | 4.0 | 0/0 | 0/1 |
| 04-relatorio | A | 5.0 | 4.0 | 0/0 | 0/0 |
| 05-relatorio | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 06-relatorio | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 07-email-cliente | A | 5.0 | 4.0 | 1/2 | 0/0 |
| 08-email-cliente | B | 4.0 | 5.0 | 0/0 | 0/0 |
| 09-apresentacao | A | 5.0 | 4.0 | 0/0 | 0/0 |
| 10-apresentacao | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 11-resposta-chat | A | 5.0 | 4.0 | 0/0 | 0/0 |
| 12-resposta-chat | A | 4.0 | 3.0 | 0/0 | 0/0 |
| controle-embraer | empate | 3.5 | 3.5 | 0/0 | 1/0 |
| controle-nubank | B | 3.0 | 4.0 | 1/0 | 0/0 |

**Resumo:** B venceu 5.5 de 14 (A 8.5). Naturalidade média A 3.96, B 3.75. Fatos perdidos A 2, B 1; inventados A 2, B 1.

## Detalhe de fidelidade

**03-post-linkedin**: A {"perdidos": [], "inventados": []}; B {"perdidos": [], "inventados": ["O professor Carlos Menezes deu orientação, apoio e contribuições durante o curso."]}

**07-email-cliente**: A {"perdidos": ["A equipe se coloca à disposição para alinhar qualquer detalhe necessário e apoiar no que for preciso para a liberação do acesso."], "inventados": ["O cliente pode indicar quem cuida da liberação do acesso.", "A equipe avançará assim que o acesso chegar."]}; B {"perdidos": [], "inventados": []}

**controle-embraer**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A Embraer nasceu no Brasil."], "inventados": []}

**controle-nubank**: A {"perdidos": ["O Nubank tem operações no Brasil."], "inventados": []}; B {"perdidos": [], "inventados": []}

