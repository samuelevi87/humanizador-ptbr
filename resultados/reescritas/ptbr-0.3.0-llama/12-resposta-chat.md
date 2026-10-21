<!-- skill: ptbr-0.3.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

Se você já usa a AWS e pretende usar o Amazon Bedrock, o Strands Agents é uma boa opção porque é um SDK integrado ao Bedrock e exige menos código de integração. Já se o seu agente tem fluxos complexos com muitas etapas condicionais ou precisa de controle explícito do estado, o LangGraph pode ser mais adequado por modelar o agente como um grafo de estados explícito.

Uma regra prática é considerar Strands Agents se você está na AWS e quer uma integração rápida, ou se quer minimizar o código de integração com serviços AWS. Por outro lado, se você precisa de controle sobre o fluxo do agente ou tem muitas retomadas, LangGraph é provavelmente melhor.

Minha recomendação é começar com Strands Agents se você quer criar agentes na AWS com pouco esforço. Se o fluxo ficar complexo demais, considere mudar para LangGraph.
