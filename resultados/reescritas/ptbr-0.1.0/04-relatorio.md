<!-- skill: ptbr-0.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Relatório técnico: redução de erros 429 na API de pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a retornar erros HTTP 429: o fornecedor limita o número de requisições e o limite estava sendo excedido.

## Causa

O fornecedor permite 60 requisições por minuto. O agente fazia até 4 chamadas por conversa para consultar estoque, sem cache, e o volume subia em horários de maior uso.

## Solução

Foi criado um cache de 5 minutos para as consultas de estoque. Respostas recentes passaram a ser reutilizadas dentro desse intervalo, e o agente deixou de chamar a API do fornecedor a cada consulta.

## Resultado

A taxa de conversas afetadas por erros 429 caiu de 18% para menos de 1%.

## Próximos passos

Manter o monitoramento da taxa de erros 429 e do volume de chamadas por minuto.
