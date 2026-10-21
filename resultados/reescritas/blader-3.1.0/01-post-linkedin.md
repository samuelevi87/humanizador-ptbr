<!-- skill: blader-3.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Em 6 semanas, uma equipe de 4 pessoas usou um modelo de linguagem para reduzir o tempo médio de triagem de chamados de suporte de 12 para 3 minutos por chamado.

Antes, a triagem era manual. Chegavam muitos chamados de categorias diferentes, e a priorização era feita à mão. Decidimos automatizar parte desse processo com IA.

O mais interessante foi o que aprendemos na primeira versão. O modelo funcionava bem na maioria das categorias, mas errava a classificação de 1 em cada 5 chamados de cobrança, justamente um tipo sensível para o negócio.

Resolvemos melhorando o contexto, sem trocar o modelo nem complicar a arquitetura. Adicionamos ao prompt exemplos reais de chamados de cobrança com a classificação correta, e isso ajudou o modelo a captar os padrões, a linguagem dos clientes e as diferenças entre categorias parecidas.

Ficaram algumas lições. Começar pequeno, com um problema bem definido e uma equipe enxuta, já gera impacto. A qualidade do prompt e dos exemplos pesa muito. Métricas simples ajudam a corrigir o rumo rapidamente. E uma boa automação não substitui o time: libera tempo para o trabalho que exige mais análise humana.
