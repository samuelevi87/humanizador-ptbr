<!-- skill: ptbr-0.3.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Decisão de arquitetura: armazenamento do histórico de conversas

## Contexto

A equipe precisava escolher onde guardar o histórico de conversas da aplicação. As opções avaliadas foram DynamoDB e PostgreSQL.

O volume previsto é de cerca de 30 mil conversas por mês. A consulta principal será buscar todas as mensagens de uma conversa pelo ID da conversa.

## Decisão

A equipe vai usar o DynamoDB para armazenar o histórico de conversas.

## Justificativa

- O acesso é simples e bem definido: buscar mensagens por ID da conversa.
- Não há consultas relacionais nem joins entre tabelas.
- O volume previsto cabe num modelo chave-valor/documento.
- O custo estimado do DynamoDB é menor para o uso atual.
- Dá para escalar se o volume de conversas crescer.

## Alternativa avaliada

O PostgreSQL foi considerado por ser um banco relacional maduro e flexível. Como o caso de uso atual não exige consultas relacionais, joins nem transações complexas, foi considerado menos adequado.

## Risco aceito

Fazer relatórios analíticos diretamente sobre os dados operacionais fica mais difícil. O DynamoDB não é indicado para consultas analíticas complexas nem para agregações flexíveis.

## Mitigação

Os dados necessários para análise serão exportados para o Amazon S3 e processados lá por ferramentas analíticas.
