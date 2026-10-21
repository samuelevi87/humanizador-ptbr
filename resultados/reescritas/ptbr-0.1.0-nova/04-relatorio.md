<!-- skill: ptbr-0.1.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

# Relatório Técnico — Redução de Erros 429 na API de Pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a retornar erros HTTP 429, indicando excesso de requisições em relação ao limite permitido pelo fornecedor.

## Causa Identificada

O fornecedor da API possui um limite de 60 requisições por minuto. Foi identificado que o agente realizava até 4 chamadas por conversa para consultas de estoque, sem utilização de cache. Esse comportamento aumentava significativamente o volume de requisições, especialmente em períodos de maior uso.

## Solução Implementada

Foi implementado um cache de 5 minutos para consultas de estoque. Com isso, respostas recentes passaram a ser reutilizadas dentro desse intervalo, reduzindo a quantidade de chamadas diretas à API do fornecedor.

## Resultado

Após a mudança, a taxa de conversas afetadas por erros 429 caiu de 18% para menos de 1%.

## Conclusão

A implementação do cache reduziu substancialmente a pressão sobre a API do fornecedor e praticamente eliminou os erros causados por limite de requisições. Recomenda-se manter o monitoramento da taxa de erros 429 e do volume de chamadas por minuto para evitar novas ocorrências.
