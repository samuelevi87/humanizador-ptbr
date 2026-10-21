<!-- skill: blader-3.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Para um catálogo de 300 produtos, em geral não vale a pena começar com banco vetorial.

Uma busca por palavra-chave com filtros costuma ser suficiente, especialmente se os produtos tiverem bons nomes, descrições, categorias e atributos.

Um banco vetorial pode ajudar se os usuários costumam buscar de forma mais "livre", descrevendo o que querem com palavras diferentes das usadas no catálogo. Por exemplo, "presente para criança que gosta de montar" em vez de "blocos de construção".

Minha recomendação é começar sem banco vetorial, usando busca textual e filtros, e acompanhar métricas como:

- buscas sem resultado;
- buscas com poucos cliques;
- termos que os usuários digitam;
- produtos que deveriam aparecer, mas não aparecem.

Se muitas buscas relevantes ficarem sem resultado por diferença de vocabulário, aí sim pode fazer sentido adicionar busca vetorial ou uma busca híbrida.
