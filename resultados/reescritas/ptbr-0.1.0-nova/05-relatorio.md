<!-- skill: ptbr-0.1.0-nova
     modelo: us.amazon.nova-pro-v1:0 -->

A equipe optou pelo DynamoDB para armazenar o histórico de conversas da aplicação. A decisão foi baseada no padrão de acesso simples, na ausência de consultas relacionais, no volume compatível com um modelo chave-valor/documento e no menor custo estimado. Embora o PostgreSQL tenha sido considerado, sua natureza relacional não se adequava ao caso de uso atual. O principal risco aceito foi a dificuldade para relatórios analíticos diretamente no DynamoDB, mitigada pela exportação dos dados para o Amazon S3 para processamento analítico.
