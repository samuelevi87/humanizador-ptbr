<!-- skill: ptbr-0.3.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

## Relatório Técnico — Lentidão no Site durante a Black Friday

### Resumo do incidente  
Na Black Friday, o tempo de resposta do site da loja aumentou de 1,2 segundo para 4,8 segundos, afetando a experiência dos usuários, especialmente na página de busca.

### Causa identificada  
A lentidão foi causada por uma consulta ao banco de dados sem índice adequado na página de busca. Essa consulta exigia mais processamento do banco, aumentando o tempo de resposta.

### Ação corretiva  
Foi criado um índice no banco de dados para otimizar a consulta usada na busca. Após a correção, o tempo de resposta foi reduzido para 1,4 segundo, próximo ao desempenho original.

### Impacto no negócio  
A loja estima que a lentidão tenha causado uma perda de aproximadamente 6% das vendas durante as duas horas em que o problema permaneceu ativo.

### Conclusão  
O incidente foi causado por uma falha de otimização em consulta de banco de dados. A criação do índice resolveu o problema e restaurou o desempenho do site. Recomenda-se revisar consultas críticas e realizar testes de carga antes de eventos de alto tráfego.
