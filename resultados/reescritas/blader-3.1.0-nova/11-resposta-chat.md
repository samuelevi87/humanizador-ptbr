<!-- skill: blader-3.1.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

RAG e fine-tuning são formas distintas de aprimorar as respostas de um modelo:

- RAG (Retrieval-Augmented Generation) recupera documentos ou informações no momento da consulta e insere esse conteúdo no contexto do modelo. É mais adequado quando as informações mudam frequentemente, pois permite atualizar a base de documentos sem retreinar o modelo.

- Fine-tuning ajusta os pesos do modelo com exemplos de treinamento. É mais indicado quando se deseja ensinar o modelo a responder em um formato, estilo ou padrão de comportamento específico.

Em resumo: RAG fornece informações atualizadas para consulta do modelo, enquanto o fine-tuning modifica o próprio modelo para responder de maneira específica.
