<!-- skill: ptbr-0.2.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Troquei um pipeline de RAG por uma busca em catálogo estruturado, e o resultado foi melhor.

O caso era responder perguntas sobre produtos a partir de um catálogo com 240 fichas em Markdown. O pipeline com busca semântica errava mais do que deveria, principalmente quando duas fichas tinham nomes quase iguais. O modelo encontrava um documento parecido, mas nem sempre o certo, e quando a recuperação vinha errada, a resposta também vinha.

Mudei a abordagem. Em vez de tratar tudo como texto solto para embeddings, organizei o catálogo como uma base estruturada, com campos claros e busca por atributos do produto.

Num conjunto de 50 perguntas, o RAG acertou 61% das respostas e a busca estruturada acertou 84%.

RAG não deveria ser a resposta automática para todo problema de busca. Quando o domínio tem dados bem delimitados, entidades conhecidas e fichas relativamente padronizadas, modelar bem o catálogo pode render mais que uma busca semântica genérica. Embeddings servem bem para significado aproximado, mas aqui eu precisava encontrar exatamente o item certo, e para isso a estrutura ainda pesa bastante.
