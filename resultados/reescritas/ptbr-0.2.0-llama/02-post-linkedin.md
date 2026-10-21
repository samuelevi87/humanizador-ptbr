<!-- skill: ptbr-0.2.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

Troquei um pipeline de RAG por busca em catálogo estruturado e o resultado melhorou. O caso era responder perguntas sobre 240 produtos em fichas Markdown. O pipeline com busca semântica errava bastante, principalmente quando duas fichas tinham nomes semelhantes, pois encontrava um documento "parecido", mas não necessariamente o correto.

Mudei a abordagem: organizei o catálogo com campos claros e busca por atributos do produto. Em 50 perguntas, a taxa de respostas corretas subiu de 61% com RAG para 84% com busca estruturada. A lição é que RAG não deve ser a solução automática para todo problema de busca. Quando o domínio tem dados delimitados e fichas padronizadas, uma boa modelagem do catálogo supera a busca semântica genérica. Embeddings são bons para significado aproximado, mas às vezes o problema é encontrar exatamente o item certo, e nesses casos a estrutura ainda é importante.
