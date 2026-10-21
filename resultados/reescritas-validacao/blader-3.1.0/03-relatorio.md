<!-- skill: blader-3.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Relatório técnico: lentidão no site durante a Black Friday

## Resumo do incidente

Durante a Black Friday, o tempo de resposta do site da loja subiu de 1,2 segundo para 4,8 segundos. A página de busca foi a mais afetada.

## Causa

A página de busca usava uma consulta ao banco de dados sem índice adequado. A consulta exigia muito processamento do banco e aumentou o tempo de resposta.

## Ação corretiva

A equipe criou um índice no banco de dados para a consulta usada na busca. Depois disso, o tempo de resposta caiu para 1,4 segundo, perto do valor original.

## Impacto no negócio

A loja estima que a lentidão tenha custado cerca de 6% das vendas durante as duas horas em que o problema esteve ativo.

## Recomendações

Revisar as consultas críticas e fazer testes de carga antes de eventos de alto tráfego.
