<!-- skill: ptbr-0.1.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

# Relatório Técnico — Redução de Erros 429 na API de Pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a dar erros HTTP 429 por excesso de requisições.

## Causa

O fornecedor limita a API a 60 requisições por minuto. O agente fazia até 4 chamadas por conversa para consultar estoque, sem usar cache, o que aumentava o volume de requisições.

## Solução

Implementamos um cache de 5 minutos para consultas de estoque. Assim, respostas recentes são reutilizadas nesse intervalo, reduzindo chamadas à API.

## Resultado

Depois da mudança, a taxa de conversas com erro 429 caiu de 18% para menos de 1%.

## Conclusão

O cache reduziu a pressão sobre a API e praticamente eliminou os erros por limite de requisições. É importante monitorar a taxa de erros 429 e o volume de chamadas por minuto para evitar que o problema volte.
