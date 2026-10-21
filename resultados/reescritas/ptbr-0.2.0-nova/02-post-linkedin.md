<!-- skill: ptbr-0.2.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

Troquei um pipeline de RAG por uma busca em catálogo estruturado e o resultado foi melhor.

O caso era simples: responder perguntas sobre produtos a partir de um catálogo com 240 fichas em Markdown. Na prática, o pipeline com busca semântica estava errando mais do que deveria, principalmente quando duas fichas tinham nomes quase iguais. O modelo encontrava um documento “parecido”, mas não necessariamente o documento certo. E, quando a recuperação vinha errada, a resposta também vinha errada.

Então mudei a abordagem: em vez de tratar tudo como texto solto para embeddings, organizei o catálogo como uma base mais estruturada, com campos claros e busca orientada por atributos do produto.

O resultado em um conjunto de 50 perguntas foi:
- Antes, com RAG: 61% de respostas corretas.
- Depois, com busca estruturada: 84% de respostas corretas.

A lição não é que RAG não funciona. A lição é que RAG não deve ser a resposta automática para todo problema de busca. Quando o domínio tem dados bem delimitados, entidades conhecidas e fichas relativamente padronizadas, uma boa modelagem do catálogo pode superar uma busca semântica genérica. Embeddings são ótimos para significado aproximado. Mas, às vezes, o problema não é “entender parecido”. É encontrar exatamente o item certo. E, nesses casos, estrutura ainda importa muito.
