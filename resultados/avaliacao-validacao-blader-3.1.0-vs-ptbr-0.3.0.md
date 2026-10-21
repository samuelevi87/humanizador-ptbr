# Avaliação: A = `blader-3.1.0` contra B = `ptbr-0.3.0`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 02-post-linkedin | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 03-relatorio | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 04-relatorio | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 05-email-cliente | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 06-email-cliente | empate | 4.5 | 4.5 | 0/0 | 0/0 |
| 07-apresentacao | A | 4.5 | 3.5 | 0/0 | 0/0 |
| 08-apresentacao | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 09-resposta-chat | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 10-resposta-chat | B | 4.0 | 5.0 | 0/0 | 0/0 |
| 11-post-linkedin | B | 3.0 | 4.0 | 0/0 | 1/0 |
| 12-relatorio | B | 3.0 | 4.0 | 0/0 | 1/1 |
| controle-blumenau | B | 3.0 | 4.0 | 0/0 | 0/0 |
| controle-petrobras | B | 2.5 | 3.5 | 0/0 | 0/0 |

**Resumo:** B venceu 10.5 de 14 (A 3.5). Naturalidade média A 3.46, B 3.96. Fatos perdidos A 0, B 2; inventados A 0, B 1.

## Detalhe de fidelidade

**11-post-linkedin**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A IA pode ajudar empresas a ganhar eficiência."], "inventados": []}

**12-relatorio**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A automação pode aumentar a satisfação dos clientes."], "inventados": ["A automação deve reduzir o volume de atendimentos manuais e o tempo de resposta, enquanto o original afirma que ela pode reduzir/melhorar esses pontos."]}

