<!-- skill: ptbr-0.3.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

# Relatório de Decisão de Arquitetura: Armazenamento do Histórico de Conversas

## Contexto

A equipe precisava definir a tecnologia de armazenamento para o histórico de conversas da aplicação. Foram avaliados o DynamoDB e o PostgreSQL. O volume previsto é de aproximadamente 30 mil conversas por mês, e a principal consulta será buscar todas as mensagens de uma conversa pelo ID.

## Decisão

A equipe escolheu o DynamoDB para armazenar o histórico de conversas.

## Justificativa

A escolha se baseou nos seguintes pontos:

- O padrão de acesso é simples: buscar mensagens por ID da conversa.
- Não há necessidade de consultas relacionais ou joins.
- O volume previsto é compatível com um modelo chave-valor/documento.
- O custo estimado do DynamoDB é menor para o uso atual.
- A solução permite escalar conforme o volume de conversas cresce.

## Alternativa Avaliada: PostgreSQL

O PostgreSQL foi considerado por ser uma solução relacional madura, mas como o caso de uso não exige consultas relacionais ou transações complexas, foi considerado menos adequado.

## Risco Aceito

O principal risco da escolha do DynamoDB é a dificuldade para fazer relatórios analíticos diretamente sobre os dados.

## Mitigação

Para mitigar esse risco, os dados serão exportados para o Amazon S3, onde poderão ser processados por ferramentas analíticas.

## Conclusão

O DynamoDB atende melhor aos requisitos atuais, considerando o padrão de acesso simples e o menor custo. A limitação para relatórios analíticos será tratada com exportações para o S3.
