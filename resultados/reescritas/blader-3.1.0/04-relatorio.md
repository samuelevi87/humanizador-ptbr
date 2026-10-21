<!-- skill: blader-3.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

# Relatório técnico: redução de erros 429 na API de pedidos

## Resumo

Em 3 de setembro, a API de pedidos começou a retornar erros HTTP 429: as requisições passaram do limite permitido pelo fornecedor.

## Causa

O fornecedor limita a API a 60 requisições por minuto. O agente fazia até 4 chamadas por conversa para consultar o estoque, sem cache, o que elevava bastante o volume de requisições nos períodos de maior uso.

## Solução

Passamos a guardar em cache por 5 minutos as consultas de estoque. Respostas recentes são reutilizadas dentro desse intervalo, e isso reduziu as chamadas diretas à API do fornecedor.

## Resultado

A taxa de conversas afetadas por erros 429 caiu de 18% para menos de 1%.

## Recomendação

Convém continuar monitorando a taxa de erros 429 e o volume de chamadas por minuto, para detectar novas ocorrências.
