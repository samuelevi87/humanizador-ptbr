# Avaliação: A = `blader-3.1.0` contra B = `ptbr-0.3.0`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 02-post-linkedin | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 03-post-linkedin | B | 3.0 | 4.0 | 0/0 | 1/0 |
| 04-relatorio | empate | 4.5 | 4.5 | 1/1 | 0/0 |
| 05-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 06-relatorio | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 07-email-cliente | A | 5.0 | 4.0 | 0/1 | 0/0 |
| 08-email-cliente | B | 4.0 | 5.0 | 0/0 | 0/1 |
| 09-apresentacao | A | 5.0 | 4.0 | 0/0 | 0/0 |
| 10-apresentacao | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 11-resposta-chat | A | 4.5 | 3.5 | 0/0 | 0/0 |
| 12-resposta-chat | A | 4.0 | 3.0 | 0/0 | 0/0 |
| controle-embraer | B | 3.0 | 4.0 | 0/0 | 1/0 |
| controle-nubank | B | 3.0 | 4.0 | 1/0 | 0/0 |

**Resumo:** B venceu 8.5 de 14 (A 5.5). Naturalidade média A 3.82, B 4.04. Fatos perdidos A 2, B 2; inventados A 2, B 1.

## Detalhe de fidelidade

**03-post-linkedin**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["O professor Carlos Menezes também foi agradecido pelas contribuições ao longo do processo."], "inventados": []}

**04-relatorio**: A {"perdidos": ["A recomendação original era manter o monitoramento para evitar novas ocorrências."], "inventados": ["A reescrita afirma que o monitoramento deve continuar para detectar novas ocorrências."]}; B {"perdidos": [], "inventados": []}

**07-email-cliente**: A {"perdidos": [], "inventados": ["O cliente pode indicar quem cuida da liberação do acesso."]}; B {"perdidos": [], "inventados": []}

**08-email-cliente**: A {"perdidos": [], "inventados": []}; B {"perdidos": [], "inventados": ["Se a tabela não for atualizada todo mês, o agente passará a responder com valores desatualizados."]}

**controle-embraer**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A pista da unidade da Embraer em Gavião Peixoto é identificada no original como o aeródromo de Gavião Peixoto."], "inventados": []}

**controle-nubank**: A {"perdidos": ["O Nubank tem operações no Brasil."], "inventados": []}; B {"perdidos": [], "inventados": []}

