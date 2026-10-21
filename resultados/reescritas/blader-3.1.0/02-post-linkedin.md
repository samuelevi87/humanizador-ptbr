<!-- skill: blader-3.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Troquei um pipeline de RAG por uma busca em catálogo estruturado, e o resultado foi melhor.

O caso era responder perguntas sobre produtos a partir de um catálogo com 240 fichas em Markdown. O pipeline com busca semântica errava mais do que deveria, principalmente quando duas fichas tinham nomes quase iguais. O modelo encontrava um documento parecido, mas nem sempre o certo, e quando a recuperação vinha errada a resposta também vinha.

Então, em vez de tratar tudo como texto solto para embeddings, organizei o catálogo como uma base estruturada, com campos claros e busca orientada por atributos do produto. Num conjunto de 50 perguntas, o RAG deu 61% de respostas corretas e a busca estruturada deu 84%.

RAG não deve ser a resposta automática para todo problema de busca. Quando o domínio tem dados bem delimitados, entidades conhecidas e fichas relativamente padronizadas, uma boa modelagem do catálogo pode superar uma busca semântica genérica. Embeddings funcionam bem para significado aproximado, mas às vezes o problema é encontrar exatamente o item certo.
