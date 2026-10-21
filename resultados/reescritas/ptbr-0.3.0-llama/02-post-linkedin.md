<!-- skill: ptbr-0.3.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

Troquei um pipeline de RAG por busca em catálogo estruturado e o resultado melhorou. O caso era responder perguntas sobre 240 produtos em fichas Markdown. O pipeline com busca semântica errava bastante, principalmente quando duas fichas tinham nomes parecidos, pois encontrava um documento "parecido", mas não necessariamente o correto.

Mudei a abordagem: organizei o catálogo com campos claros e busca orientada por atributos do produto. Com isso, a taxa de respostas corretas subiu de 61% para 84% em um conjunto de 50 perguntas.

Isso mostra que RAG não é a solução automática para todo problema de busca. Quando o domínio tem dados bem delimitados e fichas padronizadas, uma boa modelagem do catálogo pode ser melhor que uma busca semântica genérica. Embeddings são úteis para significado aproximado, mas às vezes o problema é encontrar exatamente o item certo, e nesses casos a estrutura ainda é importante.
