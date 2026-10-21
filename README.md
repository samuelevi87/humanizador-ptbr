# humanizador-ptbr

> Em construção. Ainda não use em produção.

Skill para Claude Code (e outros agentes compatíveis com Agent Skills) que reescreve texto em português do Brasil com cara de IA para que soe como quem escreveu, sem mudar o que o texto diz.

É uma adaptação do [Humanizer](https://github.com/blader/humanizer), de Siqi Chen, que por sua vez se baseia no guia [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipedia, mantido pelo WikiProject AI Cleanup. O original foi escrito para inglês: alguns padrões não valem em português (o português omite sujeito o tempo todo, e a regra de hífen é outra) e o português de LLM tem tiques próprios que o original não conhece, como "vale ressaltar", conectores no início de todo parágrafo, gerúndio em cascata, "alavancar" e "jornada".

## Como está sendo construído

O catálogo de padrões não sai de impressão pessoal. Cada padrão é validado por frequência num corpus aberto, que fica neste repositório:

- `corpus/ia/`: textos gerados por vários modelos (via Amazon Bedrock), sem instrução de estilo.
- `corpus/humano/wikipedia/`: artigos da Wikipédia lusófona na última revisão anterior a 30/11/2022, data de lançamento do ChatGPT.
- `corpus/teste/`: textos para reescrever, cada um com a lista de fatos que a reescrita precisa preservar.

Uma expressão entra no catálogo quando aparece bem mais em texto de IA do que em texto humano. A skill final é comparada com o Humanizer original em teste cego, e os resultados ficam em `resultados/`.

## Licença

MIT. Mantém o aviso de copyright do Humanizer original. Os textos em `corpus/humano/wikipedia/` são da Wikipédia, sob CC BY-SA 4.0, com atribuição no cabeçalho de cada arquivo.
