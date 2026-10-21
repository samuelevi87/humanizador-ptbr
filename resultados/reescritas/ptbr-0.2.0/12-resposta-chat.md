<!-- skill: ptbr-0.2.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Depende do contexto, mas em geral:

- Se você já está na AWS e usa ou pretende usar o Amazon Bedrock, vale considerar o Strands Agents. É um SDK da AWS, integrado nativamente ao Bedrock, então tende a exigir menos código de integração e pode ser mais simples para colocar agentes em produção na AWS.

- Se o seu agente tem fluxos complexos, com muitos desvios, etapas condicionais, retomadas, loops ou necessidade de controle explícito do estado, o LangGraph pode servir melhor. Ele modela o agente como um grafo de estados explícito, o que dá mais controle e previsibilidade sobre o comportamento.

Uma regra prática:

| Cenário | Melhor opção provável |
|---|---|
| Já está na AWS/Bedrock e quer integração rápida | Strands Agents |
| Precisa de menos código de integração com serviços AWS | Strands Agents |
| Fluxos complexos com muitos caminhos e retomadas | LangGraph |
| Quer controle explícito do estado e das transições | LangGraph |

Minha recomendação: se o objetivo é criar agentes na AWS com menos esforço operacional, comece pelo Strands Agents. Se o fluxo do agente ficar complexo demais ou exigir uma orquestração bem controlada, o LangGraph passa a valer mais a pena.
