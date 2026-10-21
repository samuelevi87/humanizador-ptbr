<!-- skill: blader-3.1.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

# Relatório de Decisão de Arquitetura: Armazenamento do Histórico de Conversas

## Contexto

A equipe precisava definir a tecnologia de armazenamento para o histórico de conversas da aplicação. As opções avaliadas foram DynamoDB e PostgreSQL. O volume previsto é de aproximadamente 30 mil conversas por mês. A consulta principal do sistema será buscar todas as mensagens associadas a uma conversa a partir do seu ID da conversa.

## Decisão

A equipe decidiu utilizar DynamoDB para armazenar o histórico de conversas.

## Justificativa

A escolha pelo DynamoDB foi baseada nos seguintes pontos: o padrão de acesso é simples e bem definido, buscar mensagens por ID da conversa; não há necessidade de consultas relacionais ou joins entre tabelas; o volume previsto é compatível com um modelo chave-valor/documento; o custo estimado do DynamoDB é menor para o cenário atual de uso; e a solução permite escalar conforme o crescimento do volume de conversas.

## Alternativa Avaliada

O PostgreSQL foi considerado por ser uma solução relacional madura e flexível. No entanto, como o caso de uso atual não exige consultas relacionais, joins ou transações complexas, ele foi considerado menos adequado.

## Risco Aceito

O principal risco aceito com a escolha do DynamoDB é a maior dificuldade para realizar relatórios analíticos diretamente sobre os dados operacionais, pois o DynamoDB não é ideal para consultas analíticas complexas ou agregações flexíveis.

## Mitigação

Para mitigar esse risco, os dados necessários para análises serão exportados para o Amazon S3, onde poderão ser processados por ferramentas analíticas apropriadas.

## Conclusão

A escolha do DynamoDB atende melhor aos requisitos atuais da aplicação, considerando o padrão de acesso simples, a ausência de consultas relacionais e o menor custo previsto. A limitação para relatórios analíticos foi aceita e será tratada por meio de exportações para o S3.
