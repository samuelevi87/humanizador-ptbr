<!-- skill: ptbr-0.3.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

Para um catálogo de 300 produtos, geralmente não vale a pena começar com banco vetorial, pois uma busca por palavra-chave com filtros costuma ser suficiente, especialmente se os produtos tiverem bons nomes, descrições, categorias e atributos.

Um banco vetorial pode ser útil se os usuários buscam de forma mais livre, descrevendo o que querem com palavras diferentes das usadas no catálogo. Por exemplo, alguém pode procurar por "presente para criança que gosta de montar" em vez de "blocos de construção".

Minha recomendação é começar sem banco vetorial, usando busca textual e filtros. Acompanhe métricas como buscas sem resultado, buscas com poucos cliques, termos que os usuários digitam e produtos que deveriam aparecer mas não aparecem. Se muitas buscas relevantes ficarem sem resultado por causa de diferenças de vocabulário, pode fazer sentido adicionar busca vetorial ou uma busca híbrida.
