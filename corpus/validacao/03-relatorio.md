<!-- modelo: us.openai.gpt-5.5
     data: 2026-10-21
     pedido: Escreva um relatório técnico curto com estas informações. -->

## Relatório Técnico — Lentidão no Site durante a Black Friday

### 1. Resumo do incidente  
Durante a Black Friday, o tempo de resposta do site da loja aumentou de **1,2 segundo para 4,8 segundos**, impactando a experiência dos usuários, especialmente na página de busca.

### 2. Causa identificada  
A análise técnica identificou que a lentidão foi causada por uma **consulta ao banco de dados sem índice adequado** na página de busca. Essa consulta exigia maior processamento do banco, aumentando significativamente o tempo de resposta.

### 3. Ação corretiva  
Foi criado um **índice no banco de dados** para otimizar a consulta utilizada na busca. Após a correção, o tempo de resposta foi reduzido para **1,4 segundo**, próximo ao desempenho original.

### 4. Impacto no negócio  
A loja estima que a lentidão tenha causado uma perda de aproximadamente **6% das vendas** durante as **duas horas** em que o problema permaneceu ativo.

### 5. Conclusão  
O incidente foi causado por uma falha de otimização em consulta de banco de dados. A criação do índice resolveu o problema e restaurou o desempenho do site. Recomenda-se revisar consultas críticas e realizar testes de carga antes de eventos de alto tráfego.
