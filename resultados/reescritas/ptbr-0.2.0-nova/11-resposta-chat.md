<!-- skill: ptbr-0.2.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

RAG e fine-tuning são abordagens distintas para aprimorar as respostas de um modelo:

- **RAG** (*Retrieval-Augmented Generation*) busca documentos ou informações no momento da pergunta e os inclui no contexto do modelo. É ideal para situações em que as informações mudam frequentemente, pois permite atualizar a base de documentos sem a necessidade de retreinar o modelo.

- **Fine-tuning** ajusta os pesos do modelo com base em exemplos de treinamento. É mais adequado quando o objetivo é ensinar o modelo a responder em um formato, estilo ou padrão de comportamento específico.

Em resumo, RAG fornece informações atualizadas para o modelo consultar, enquanto o fine-tuning modifica o próprio modelo para responder de uma maneira específica.
