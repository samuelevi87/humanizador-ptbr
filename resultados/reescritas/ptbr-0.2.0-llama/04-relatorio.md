<!-- skill: ptbr-0.2.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

# Relatório Técnico — Redução de Erros 429 na API de Pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a dar erros HTTP 429 por excesso de requisições.

## Causa Identificada

O fornecedor da API permite até 60 requisições por minuto. O agente fazia até 4 chamadas por conversa para consultar estoque, sem usar cache, o que aumentava muito o volume de requisições.

## Solução Implementada

Foi adicionado um cache de 5 minutos para consultas de estoque. Assim, respostas recentes são reutilizadas nesse intervalo, reduzindo as chamadas à API do fornecedor.

## Resultado

Depois da mudança, a taxa de conversas com erros 429 caiu de 18% para menos de 1%.

## Conclusão

O cache reduziu a pressão sobre a API do fornecedor e praticamente eliminou os erros por limite de requisições. É recomendável continuar monitorando a taxa de erros 429 e o volume de chamadas por minuto.
