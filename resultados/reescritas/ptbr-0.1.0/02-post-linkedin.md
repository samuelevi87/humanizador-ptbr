<!-- skill: ptbr-0.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Troquei um pipeline de RAG por uma busca em catálogo estruturado, e o resultado foi melhor.

O caso era responder perguntas sobre produtos a partir de um catálogo com 240 fichas em Markdown.

O pipeline com busca semântica errava mais do que deveria, principalmente quando duas fichas tinham nomes quase iguais. O modelo encontrava um documento parecido, mas nem sempre o certo, e quando a recuperação vinha errada, a resposta também vinha.

Em vez de tratar tudo como texto solto para embeddings, organizei o catálogo como uma base estruturada, com campos claros e busca por atributos do produto.

Num conjunto de 50 perguntas, as respostas corretas foram de 61% com RAG para 84% com busca estruturada.

RAG não deve ser a resposta automática para todo problema de busca. Quando os dados são bem delimitados, as entidades são conhecidas e as fichas são relativamente padronizadas, modelar bem o catálogo pode superar uma busca semântica genérica. Embeddings servem para significado aproximado, e aqui eu precisava encontrar exatamente o item certo.
