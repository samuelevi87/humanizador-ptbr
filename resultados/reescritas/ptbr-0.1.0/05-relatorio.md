<!-- skill: ptbr-0.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Decisão de arquitetura: armazenamento do histórico de conversas

## Contexto

A equipe precisava escolher onde guardar o histórico de conversas da aplicação. As opções eram DynamoDB e PostgreSQL.

O volume previsto é de cerca de 30 mil conversas por mês. A consulta principal busca todas as mensagens de uma conversa pelo ID da conversa.

## Decisão

A equipe vai usar DynamoDB.

## Justificativa

- O acesso é simples e bem definido: buscar mensagens por ID da conversa.
- Não há consultas relacionais nem joins entre tabelas.
- O volume previsto cabe bem num modelo chave-valor/documento.
- O custo estimado do DynamoDB é menor para o uso atual.
- Dá para escalar se o volume de conversas crescer.

## Alternativa avaliada

O PostgreSQL foi considerado por ser um banco relacional maduro e flexível. Como o caso de uso atual não exige consultas relacionais, joins nem transações complexas, a equipe o achou menos adequado aqui.

## Risco aceito

Com o DynamoDB, fica mais difícil gerar relatórios analíticos direto sobre os dados operacionais. Ele não serve bem para consultas analíticas complexas nem para agregações flexíveis.

## Mitigação

Os dados necessários para análise serão exportados para o Amazon S3, onde ferramentas analíticas podem processá-los.

## Conclusão

O DynamoDB atende melhor os requisitos atuais: o acesso é simples, não há consultas relacionais e o custo previsto é menor. A equipe aceitou a limitação para relatórios analíticos e vai tratá-la com exportações para o S3.
