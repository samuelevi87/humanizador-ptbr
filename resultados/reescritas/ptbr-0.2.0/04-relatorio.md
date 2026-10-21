<!-- skill: ptbr-0.2.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Relatório técnico: redução de erros 429 na API de pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a retornar erros HTTP 429: as requisições passaram do limite permitido pelo fornecedor.

## Causa

O fornecedor da API limita o uso a 60 requisições por minuto. O agente fazia até 4 chamadas por conversa para consultar estoque, sem cache, e isso elevava o volume de requisições nos horários de maior uso.

## Solução

Foi criado um cache de 5 minutos para as consultas de estoque. Respostas recentes são reaproveitadas dentro desse intervalo, e o agente chama a API do fornecedor menos vezes.

## Resultado

A taxa de conversas afetadas por erros 429 caiu de 18% para menos de 1%.

## Próximos passos

Continuar monitorando a taxa de erros 429 e o volume de chamadas por minuto, para detectar novas ocorrências.
