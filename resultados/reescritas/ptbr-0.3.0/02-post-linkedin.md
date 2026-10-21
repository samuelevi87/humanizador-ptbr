<!-- skill: ptbr-0.3.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Troquei um pipeline de RAG por uma busca em catálogo estruturado, e o resultado foi melhor.

O caso era responder perguntas sobre produtos a partir de um catálogo com 240 fichas em Markdown.

O pipeline com busca semântica errava mais do que devia, principalmente quando duas fichas tinham nomes quase iguais. O modelo encontrava um documento parecido, mas nem sempre o certo, e quando a recuperação vinha errada a resposta também vinha.

Então reorganizei o catálogo em campos claros e passei a buscar por atributos do produto, em vez de tratar tudo como texto solto para embeddings.

Num conjunto de 50 perguntas, as respostas corretas subiram de 61% com RAG para 84% com a busca estruturada.

RAG continua útil, mas não deveria ser a resposta automática para todo problema de busca. Quando os dados são bem delimitados, as entidades são conhecidas e as fichas relativamente padronizadas, modelar bem o catálogo pode render mais que uma busca semântica genérica. Embeddings servem para significado aproximado, e aqui eu precisava encontrar exatamente o item certo.
