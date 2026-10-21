# Avaliação: A = `blader-3.1.0-llama` contra B = `ptbr-0.3.0-llama`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | B | 2.0 | 3.0 | 3/1 | 3/0 |
| 02-post-linkedin | B | 3.5 | 4.5 | 1/0 | 3/0 |
| 03-post-linkedin | B | 3.0 | 4.0 | 2/0 | 2/0 |
| 04-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 05-relatorio | B | 3.0 | 4.0 | 0/0 | 1/0 |
| 06-relatorio | B | 3.5 | 4.5 | 0/0 | 0/0 |
| 07-email-cliente | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 08-email-cliente | B | 3.0 | 4.5 | 1/0 | 1/0 |
| 09-apresentacao | B | 2.0 | 3.5 | 0/0 | 0/0 |
| 10-apresentacao | B | 2.0 | 3.0 | 2/0 | 0/0 |
| 11-resposta-chat | B | 3.0 | 4.0 | 0/0 | 1/0 |
| 12-resposta-chat | B | 3.0 | 4.0 | 1/0 | 4/0 |
| controle-embraer | B | 3.0 | 4.0 | 0/0 | 3/2 |
| controle-nubank | B | 3.0 | 4.0 | 3/1 | 4/1 |

**Resumo:** B venceu 14.0 de 14 (A 0.0). Naturalidade média A 2.86, B 3.93. Fatos perdidos A 13, B 22; inventados A 2, B 3.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": ["Havia muitos chamados chegando no cenário inicial.", "A solução não foi trocar o modelo.", "A solução não foi aumentar a complexidade da arquitetura."], "inventados": ["O tempo médio de 12 minutos era devido à priorização manual e às categorias variadas."]}; B {"perdidos": ["A solução não foi trocar o modelo.", "A solução não foi aumentar a complexidade da arquitetura.", "Os exemplos ajudaram o modelo a entender melhor as diferenças entre categorias parecidas."], "inventados": []}

**02-post-linkedin**: A {"perdidos": ["O domínio citado também envolve fichas relativamente padronizadas."], "inventados": []}; B {"perdidos": ["Antes da mudança, o catálogo era tratado como texto solto para embeddings.", "Quando a recuperação vinha errada, a resposta também vinha errada.", "O domínio citado incluía entidades conhecidas."], "inventados": []}

**03-post-linkedin**: A {"perdidos": ["O estudo analisava a efetividade dos sistemas em contextos reais de interação com usuários.", "O professor Carlos Menezes também foi agradecido por suas contribuições ao longo do processo."], "inventados": []}; B {"perdidos": ["O estudo no trabalho de conclusão considerava contextos reais de interação com usuários.", "O professor Carlos Menezes também fez contribuições ao longo do processo."], "inventados": []}

**05-relatorio**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["O DynamoDB não é ideal para consultas analíticas complexas ou agregações flexíveis, diferentemente de um banco relacional."], "inventados": []}

**08-email-cliente**: A {"perdidos": ["O cliente perguntou se o agente pode responder sobre preços."], "inventados": []}; B {"perdidos": ["A atualização mensal da planilha tem como finalidade garantir que as informações fornecidas estejam sempre corretas."], "inventados": []}

**10-apresentacao**: A {"perdidos": ["A alça dobrável também facilita o armazenamento.", "É ideal para café, chá, água, sucos e outras bebidas."], "inventados": []}; B {"perdidos": [], "inventados": []}

**11-resposta-chat**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["Fine-tuning ajusta os pesos do modelo."], "inventados": []}

**12-resposta-chat**: A {"perdidos": ["Strands Agents é um SDK da AWS."], "inventados": []}; B {"perdidos": ["Strands Agents pode ser mais simples para colocar agentes em produção dentro do ecossistema AWS.", "O original cita loops como um tipo de complexidade de fluxo em que LangGraph pode ser mais adequado.", "LangGraph dá mais previsibilidade sobre o comportamento do agente.", "O original menciona controle explícito das transições, além do estado."], "inventados": []}

**controle-embraer**: A {}; B {"perdidos": ["As unidades industriais, escritórios e centros de distribuição são estabelecidos para atender demandas globais.", "No aeroporto de São José dos Campos, toda a infraestrutura é compartilhada e mantida em parceria com a Infraero.", "A pista da unidade de Gavião Peixoto é identificada como aeródromo de Gavião Peixoto."], "inventados": ["A pista do aeroporto de São José dos Campos é compartilhada com a Infraero para transporte aéreo comercial.", "A pista de Gavião Peixoto é afirmada como a mais longa da América Latina, enquanto o original diz que ela é considerada a mais longa pista de pousos da América Latina."]}

**controle-nubank**: A {"perdidos": ["A empresa tem operações no Brasil.", "A empresa é sediada em São Paulo.", "A conta digital do Nubank era anteriormente denominada NuConta."], "inventados": ["A empresa foi fundada em São Paulo."]}; B {"perdidos": ["Que o Nubank atua como operadora de cartões de crédito e fintech.", "Que o Nubank tem operações no Brasil.", "Que o Nubank é sediado em São Paulo.", "Que a conta digital do Nubank era anteriormente denominada NuConta."], "inventados": ["Que o Nubank foi fundado em São Paulo."]}

