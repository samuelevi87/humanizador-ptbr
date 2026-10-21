<!-- modelo: us.openai.gpt-5.5
     data: 2026-10-21
     pedido: Responda à pergunta do usuário usando estas informações. -->

Para um catálogo de **300 produtos**, em geral **não vale a pena começar com banco vetorial**.

Uma **busca por palavra-chave com filtros** costuma ser suficiente, especialmente se os produtos tiverem bons nomes, descrições, categorias e atributos.

Um banco vetorial pode ajudar se os usuários costumam buscar de forma mais “livre”, por exemplo descrevendo o que querem com palavras diferentes das usadas no catálogo — tipo “presente para criança que gosta de montar” em vez de “blocos de construção”.

Minha recomendação: **comece sem banco vetorial**, usando busca textual e filtros, e acompanhe métricas como:

- buscas sem resultado;
- buscas com poucos cliques;
- termos que os usuários digitam;
- produtos que deveriam aparecer, mas não aparecem.

Se muitas buscas relevantes ficarem sem resultado por diferença de vocabulário, aí sim pode fazer sentido adicionar busca vetorial ou uma busca híbrida.
