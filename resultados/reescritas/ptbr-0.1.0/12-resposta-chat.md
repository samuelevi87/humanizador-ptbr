<!-- skill: ptbr-0.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Depende do contexto, mas em geral:

Se você já está na AWS e usa (ou pretende usar) o Amazon Bedrock, vale considerar o Strands Agents. É um SDK da AWS integrado nativamente ao Bedrock, então tende a exigir menos código de integração e pode ser mais simples para colocar agentes em produção na AWS.

Se o agente tem fluxos complexos, com muitos desvios, etapas condicionais, retomadas, loops ou necessidade de controle explícito do estado, o LangGraph pode servir melhor. Ele modela o agente como um grafo de estados explícito, o que dá mais controle e previsibilidade sobre o comportamento.

Na prática: para criar agentes dentro da AWS com menos esforço operacional, comece pelo Strands Agents. Se o fluxo ficar complexo demais ou exigir uma orquestração muito controlada, aí o LangGraph pode valer mais a pena.
