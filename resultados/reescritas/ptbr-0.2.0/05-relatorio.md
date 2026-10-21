<!-- skill: ptbr-0.2.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Decisão de arquitetura: armazenamento do histórico de conversas

## Contexto

A equipe precisava escolher onde guardar o histórico de conversas da aplicação. As opções avaliadas foram DynamoDB e PostgreSQL.

O volume previsto é de cerca de 30 mil conversas por mês. A consulta principal do sistema vai buscar todas as mensagens de uma conversa a partir do ID da conversa.

## Decisão

A equipe vai usar DynamoDB para armazenar o histórico de conversas.

## Justificativa

- O acesso é simples e bem definido: buscar mensagens por ID da conversa.
- Não há consultas relacionais nem joins entre tabelas.
- O volume previsto cabe bem em um modelo chave-valor/documento.
- O custo estimado do DynamoDB é menor para o uso atual.
- Dá para escalar se o volume de conversas crescer.

## Alternativa avaliada

O PostgreSQL foi considerado por ser um banco relacional maduro e flexível. Como o caso de uso atual não exige consultas relacionais, joins nem transações complexas, ele foi julgado menos adequado a este cenário.

## Risco aceito

O principal risco da escolha é a maior dificuldade para gerar relatórios analíticos direto dos dados operacionais. O DynamoDB, ao contrário de um banco relacional, não é ideal para consultas analíticas complexas nem para agregações flexíveis.

## Mitigação

Os dados necessários para análise serão exportados para o Amazon S3, onde ferramentas analíticas poderão processá-los.

## Conclusão

O DynamoDB atende melhor os requisitos atuais: o padrão de acesso é simples, não há consultas relacionais e o custo previsto é menor. A equipe aceitou a limitação para relatórios analíticos e vai contorná-la com exportações para o S3.
