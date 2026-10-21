<!-- skill: blader-3.1.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

# Relatório Técnico — Redução de Erros 429 na API de Pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a retornar erros HTTP 429 devido ao excesso de requisições em relação ao limite permitido pelo fornecedor.

## Causa Identificada

O fornecedor da API tem um limite de 60 requisições por minuto. O agente fazia até 4 chamadas por conversa para verificar o estoque sem usar cache, aumentando o volume de requisições, especialmente nos períodos de maior uso.

## Solução Implementada

Implementamos um cache de 5 minutos para as consultas de estoque. Com isso, as respostas recentes são reutilizadas dentro desse intervalo, reduzindo as chamadas diretas à API do fornecedor.

## Resultado

Depois da mudança, a taxa de conversas com erros 429 caiu de 18% para menos de 1%.

## Conclusão

O cache reduziu a pressão sobre a API do fornecedor e praticamente eliminou os erros por limite de requisições. É recomendável monitorar a taxa de erros 429 e o volume de chamadas por minuto para evitar novos problemas.
