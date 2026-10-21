<!-- skill: ptbr-0.3.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

# Relatório de Decisão de Arquitetura: Armazenamento do Histórico de Conversas

## Contexto

A equipe precisava escolher a tecnologia de armazenamento para o histórico de conversas da aplicação. As opções foram DynamoDB e PostgreSQL.

O volume previsto é de aproximadamente 30 mil conversas por mês. O sistema buscará todas as mensagens associadas a uma conversa a partir do ID da conversa.

## Decisão

A equipe decidiu usar DynamoDB para armazenar o histórico de conversas.

## Justificativa

A escolha pelo DynamoDB foi baseada nos seguintes pontos:

- O padrão de acesso é simples: buscar mensagens por ID da conversa.
- Não há necessidade de consultas relacionais ou joins.
- O volume previsto é compatível com um modelo chave-valor/documento.
- O custo estimado do DynamoDB é menor para o cenário atual de uso.
- A solução permite escalar conforme o crescimento do volume de conversas.

## Alternativa Avaliada

### PostgreSQL

O PostgreSQL foi considerado por ser uma solução relacional madura e flexível. No entanto, como o caso de uso atual não exige consultas relacionais, joins ou transações complexas, ele foi considerado menos adequado para este cenário específico.

## Risco Aceito

O principal risco aceito com a escolha do DynamoDB é a maior dificuldade para realizar relatórios analíticos diretamente sobre os dados operacionais. Diferente de um banco relacional, o DynamoDB não é ideal para consultas analíticas complexas ou agregações flexíveis.

## Mitigação

Para mitigar esse risco, os dados necessários para análises serão exportados para o Amazon S3, onde poderão ser processados por ferramentas analíticas apropriadas.

## Conclusão

A escolha do DynamoDB atende melhor aos requisitos atuais da aplicação, considerando o padrão de acesso simples, a ausência de consultas relacionais e o menor custo previsto. A limitação para relatórios analíticos foi aceita pela equipe e será tratada por meio de exportações para o S3.
