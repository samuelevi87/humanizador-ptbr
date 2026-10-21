<!-- skill: ptbr-0.2.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

Depende do seu contexto, mas em geral:

- Se você já está na AWS e usa ou pretende usar o Amazon Bedrock, vale bastante considerar o Strands Agents. É um SDK da AWS, integrado nativamente ao Bedrock, então tende a exigir menos código de integração e pode ser mais simples para colocar agentes em produção dentro do ecossistema AWS.
- Se o seu agente tem fluxos complexos, com muitos desvios, etapas condicionais, retomadas, loops ou necessidade de controle explícito do estado, o LangGraph pode ser mais adequado. Ele modela o agente como um grafo de estados explícito, o que dá mais controle e previsibilidade sobre o comportamento.

Uma regra prática:

| Cenário                                          | Melhor opção provável      |
| ------------------------------------------------ | -------------------------- |
| Já está na AWS/Bedrock e quer integração rápida  | Strands Agents             |
| Precisa de menos código de integração com serviços AWS | Strands Agents             |
| Fluxos complexos com muitos caminhos e retomadas | LangGraph                  |
| Quer controle explícito do estado e das transições | LangGraph                  |

Minha recomendação:  
Se o objetivo é criar agentes dentro da AWS com menor esforço operacional, comece com o Strands Agents. Se você perceber que o fluxo do agente está ficando complexo demais ou precisa de orquestração muito controlada, aí o LangGraph pode valer mais a pena.
