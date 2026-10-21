<!-- skill: ptbr-0.1.0-llama
     modelo: us.meta.llama4-maverick-17b-instruct-v1:0 -->

Modelos podem ser melhorados de duas formas: RAG e fine-tuning. O RAG (*Retrieval-Augmented Generation*) busca informações atualizadas no momento da pergunta e as usa junto com o contexto do modelo. Isso é útil quando a informação muda com frequência, pois você pode atualizar a base de documentos sem precisar treinar o modelo novamente.

Já o fine-tuning ajusta os pesos do modelo com exemplos de treino. Ele é mais adequado quando você quer que o modelo responda num formato, estilo ou padrão de comportamento específico.

O RAG traz informação atualizada para o modelo consultar, enquanto o fine-tuning muda o modelo para que ele responda de uma certa maneira.
