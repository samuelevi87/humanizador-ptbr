<!-- skill: ptbr-0.3.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

## Relatório Técnico — Lentidão no Site durante a Black Friday

### 1. Resumo do incidente  
Durante a Black Friday, o tempo de resposta do site da loja subiu de 1,2 para 4,8 segundos, afetando principalmente a página de busca.

### 2. Causa identificada  
A lentidão foi causada por uma consulta ao banco de dados da página de busca que não tinha índice adequado. Isso exigiu mais processamento do banco e aumentou o tempo de resposta.

### 3. Ação corretiva  
Um índice foi criado no banco de dados para otimizar a consulta de busca. Com a correção, o tempo de resposta caiu para 1,4 segundo.

### 4. Impacto no negócio  
A loja estima que a lentidão tenha custado cerca de 6% das vendas durante as duas horas em que o problema durou.

### 5. Conclusão  
O problema foi causado por falta de otimização em consulta de banco de dados. A criação do índice resolveu o problema. É recomendado revisar consultas críticas e fazer testes de carga antes de eventos com muito tráfego.
