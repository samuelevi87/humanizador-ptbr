# Fatos que a reescrita precisa preservar

- Uma API de pedidos começou a devolver erro 429 em 3 de setembro.
- O limite do fornecedor é de 60 requisições por minuto.
- O agente fazia até 4 chamadas por conversa, sem cache.
- A solução foi um cache de 5 minutos para consultas de estoque.
- Depois da mudança, os erros 429 caíram de 18% para menos de 1% das conversas.
