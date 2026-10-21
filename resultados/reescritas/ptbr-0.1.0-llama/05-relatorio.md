<!-- skill: ptbr-0.1.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

# Relatório de Decisão de Arquitetura: Armazenamento do Histórico de Conversas

## Contexto

A equipe precisava definir a tecnologia de armazenamento para o histórico de conversas da aplicação. Foram avaliados o DynamoDB e o PostgreSQL para armazenar cerca de 30 mil conversas por mês. O sistema precisará buscar todas as mensagens de uma conversa pelo ID da conversa.

## Decisão

A equipe escolheu o DynamoDB para armazenar o histórico de conversas.

## Justificativa

A escolha se baseou no padrão de acesso simples, que é buscar mensagens por ID da conversa, e na ausência de consultas relacionais. O volume previsto é compatível com o modelo chave-valor/documento do DynamoDB, e o custo estimado é menor para o uso atual. Além disso, a solução escala conforme o volume de conversas cresce.

## Alternativa Avaliada

O PostgreSQL foi considerado por ser uma solução relacional madura, mas como o caso de uso não exige consultas relacionais ou transações complexas, foi considerado menos adequado.

## Risco Aceito

O principal risco da escolha do DynamoDB é a dificuldade para fazer relatórios analíticos diretamente sobre os dados.

## Mitigação

Para mitigar esse risco, os dados serão exportados para o Amazon S3, onde poderão ser processados por ferramentas analíticas.

## Conclusão

O DynamoDB atende aos requisitos da aplicação devido ao padrão de acesso simples e ao menor custo. A equipe aceitou a limitação para relatórios analíticos e irá exportar os dados para o S3.
