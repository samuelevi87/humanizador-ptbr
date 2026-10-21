<!-- skill: ptbr-0.3.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Relatório técnico: redução de erros 429 na API de pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a retornar erros HTTP 429: as requisições passaram do limite permitido pelo fornecedor.

## Causa

O fornecedor limita a API a 60 requisições por minuto. O agente fazia até 4 chamadas por conversa para consultar estoque, sem cache, e o volume subia muito nos horários de maior uso.

## Solução

Colocamos um cache de 5 minutos nas consultas de estoque. Respostas recentes são reaproveitadas dentro desse intervalo, e a API do fornecedor recebe menos chamadas diretas.

## Resultado

A taxa de conversas afetadas por erros 429 caiu de 18% para menos de 1%.

## Conclusão

O cache reduziu bastante a pressão sobre a API do fornecedor e quase eliminou os erros por limite de requisições. Convém seguir acompanhando a taxa de erros 429 e o volume de chamadas por minuto, para detectar cedo uma recorrência.
