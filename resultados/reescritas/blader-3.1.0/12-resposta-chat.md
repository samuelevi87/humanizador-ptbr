<!-- skill: blader-3.1.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

Depende do seu contexto.

Se você já está na AWS e usa ou pretende usar o Amazon Bedrock, vale considerar o Strands Agents. Ele é um SDK da AWS integrado nativamente ao Bedrock, então tende a exigir menos código de integração e pode ser mais simples para colocar agentes em produção dentro do ecossistema AWS.

Se o seu agente tem fluxos complexos, com muitos desvios, etapas condicionais, retomadas, loops ou necessidade de controle explícito do estado, o LangGraph pode ser mais adequado. Ele modela o agente como um grafo de estados explícito, o que dá mais controle e previsibilidade sobre o comportamento.

Minha recomendação: se o objetivo é criar agentes dentro da AWS com menor esforço operacional, comece pelo Strands Agents. Se o fluxo ficar complexo demais ou exigir uma orquestração muito controlada, o LangGraph passa a compensar.
