<!-- skill: ptbr-0.3.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

## Relatório técnico: lentidão no site durante a Black Friday

### 1. Resumo do incidente

Durante a Black Friday, o tempo de resposta do site da loja subiu de 1,2 segundo para 4,8 segundos. A página de busca foi a mais afetada.

### 2. Causa

A lentidão veio de uma consulta ao banco de dados sem índice adequado na página de busca. A consulta exigia muito processamento do banco e aumentava o tempo de resposta.

### 3. Correção

Criamos um índice no banco para a consulta usada na busca. Depois disso, o tempo de resposta caiu para 1,4 segundo, perto do original.

### 4. Impacto no negócio

A loja estima ter perdido cerca de 6% das vendas nas duas horas em que o problema durou.

### 5. Conclusão

O incidente veio de uma consulta mal otimizada no banco de dados, e o índice resolveu o problema. Recomenda-se revisar as consultas críticas e fazer testes de carga antes de eventos de alto tráfego.
