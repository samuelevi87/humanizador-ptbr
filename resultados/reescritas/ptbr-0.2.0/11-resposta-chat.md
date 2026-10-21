<!-- skill: ptbr-0.2.0
     modelo: us.anthropic.claude-sonnet-5-5 -->

RAG e fine-tuning são duas formas de melhorar as respostas de um modelo.

O RAG (*Retrieval-Augmented Generation*) busca documentos ou informações no momento da pergunta e coloca esse conteúdo no contexto do modelo. Funciona melhor quando a informação muda com frequência, porque dá para atualizar a base de documentos sem treinar o modelo de novo.

O fine-tuning ajusta os pesos do modelo com exemplos de treino. Serve mais quando você quer que o modelo responda em um formato, estilo ou padrão de comportamento específico.

Ou seja, o RAG dá ao modelo informação atualizada para consultar, e o fine-tuning muda o próprio modelo para responder de determinada maneira.
