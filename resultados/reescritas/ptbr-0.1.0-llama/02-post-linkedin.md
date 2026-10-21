<!-- skill: ptbr-0.1.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

Troquei um pipeline de RAG por busca em catálogo estruturado e o resultado melhorou.

O caso era responder perguntas sobre produtos a partir de um catálogo com 240 fichas em Markdown. O pipeline com busca semântica errava bastante, principalmente quando duas fichas tinham nomes quase iguais. O modelo encontrava um documento “parecido”, mas não necessariamente o certo, e a resposta vinha errada junto com a recuperação.

Mudei a abordagem: organizei o catálogo como uma base estruturada, com campos claros e busca orientada por atributos do produto. Com um conjunto de 50 perguntas, a taxa de respostas corretas subiu de 61% com RAG para 84% com busca estruturada.

Isso não significa que RAG não funciona. Significa que não deve ser a resposta automática para todo problema de busca. Quando o domínio tem dados bem delimitados e fichas padronizadas, uma boa modelagem do catálogo pode superar uma busca semântica genérica. Embeddings são bons para significado aproximado, mas às vezes o problema é encontrar exatamente o item certo, e nesses casos a estrutura ainda importa.
