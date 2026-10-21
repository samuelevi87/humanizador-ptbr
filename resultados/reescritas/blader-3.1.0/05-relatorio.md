<!-- skill: blader-3.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Relatório de decisão de arquitetura: armazenamento do histórico de conversas

## Contexto

A equipe precisava escolher a tecnologia de armazenamento para o histórico de conversas da aplicação. As opções avaliadas foram DynamoDB e PostgreSQL.

O volume previsto é de cerca de 30 mil conversas por mês. A consulta principal busca todas as mensagens de uma conversa a partir do ID da conversa.

## Decisão

A equipe decidiu usar o DynamoDB para armazenar o histórico de conversas.

## Justificativa

O padrão de acesso é simples e bem definido: buscar mensagens por ID da conversa. Não há consultas relacionais nem joins entre tabelas, e o volume previsto é compatível com um modelo chave-valor/documento. O custo estimado do DynamoDB também é menor para o uso atual, e a solução escala conforme o volume de conversas crescer.

## Alternativa avaliada

O PostgreSQL foi considerado por ser uma solução relacional madura e flexível. Como o caso de uso atual não exige consultas relacionais, joins nem transações complexas, a equipe o considerou menos adequado.

## Risco aceito

O principal risco é a maior dificuldade de gerar relatórios analíticos diretamente sobre os dados operacionais, já que o DynamoDB não é ideal para consultas analíticas complexas nem para agregações flexíveis.

## Mitigação

Os dados necessários para análises serão exportados para o Amazon S3, onde ferramentas analíticas poderão processá-los.
