# Fatos que a reescrita precisa preservar

- A equipe precisava escolher entre DynamoDB e PostgreSQL para guardar o histórico de conversas.
- O volume previsto é de 30 mil conversas por mês.
- A consulta mais comum é buscar todas as mensagens de uma conversa pelo ID.
- A equipe escolheu DynamoDB porque não há consultas relacionais e o custo previsto é menor.
- O risco aceito é a dificuldade de fazer relatórios analíticos, que serão feitos exportando para o S3.
