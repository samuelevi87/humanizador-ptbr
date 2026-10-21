<!-- skill: ptbr-0.2.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

# Relatório de Decisão de Arquitetura: Armazenamento do Histórico de Conversas

## Contexto

A equipe precisava definir a tecnologia de armazenamento para o histórico de conversas da aplicação. Foram avaliados o DynamoDB e o PostgreSQL para armazenar cerca de 30 mil conversas por mês. O sistema precisará buscar todas as mensagens de uma conversa pelo ID da conversa.

## Decisão

A equipe escolheu o DynamoDB para armazenar o histórico de conversas.

## Justificativa

A escolha se baseou no padrão de acesso simples, que envolve buscar mensagens por ID da conversa, sem necessidade de consultas relacionais ou joins. O volume previsto é compatível com um modelo chave-valor/documento, e o custo estimado do DynamoDB é menor para o cenário atual. Além disso, a solução permite escalar conforme o volume de conversas cresce.

## Alternativa Avaliada

O PostgreSQL foi considerado por ser uma solução relacional madura, mas não foi escolhido porque o caso de uso não exige consultas relacionais, joins ou transações complexas.

## Risco Aceito

O principal risco da escolha do DynamoDB é a dificuldade para fazer relatórios analíticos diretamente sobre os dados. O DynamoDB não é ideal para consultas analíticas complexas.

## Mitigação

Para mitigar esse risco, os dados serão exportados para o Amazon S3, onde poderão ser processados por ferramentas analíticas.

## Conclusão

O DynamoDB atende aos requisitos da aplicação devido ao seu padrão de acesso simples, ausência de consultas relacionais e menor custo. A equipe aceitou a limitação para relatórios analíticos e irá exportar os dados para o S3.
