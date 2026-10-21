<!-- modelo: us.openai.gpt-5.5
     data: 2026-10-21
     pedido: Responda à pergunta do usuário usando estas informações. -->

RAG e fine-tuning são formas diferentes de melhorar as respostas de um modelo:

- **RAG** (*Retrieval-Augmented Generation*) busca documentos ou informações **no momento da pergunta** e coloca esse conteúdo no contexto do modelo. É melhor quando a informação muda com frequência, porque você pode atualizar a base de documentos sem treinar o modelo novamente.

- **Fine-tuning** ajusta os **pesos do modelo** usando exemplos de treino. Ele é mais indicado quando você quer ensinar o modelo a responder em um certo **formato, estilo ou padrão de comportamento**.

Em resumo: **RAG traz informação atualizada para o modelo consultar**, enquanto **fine-tuning muda o próprio modelo para responder de uma determinada maneira**.
