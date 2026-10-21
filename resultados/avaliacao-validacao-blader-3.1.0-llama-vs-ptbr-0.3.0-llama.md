# Avaliação: A = `blader-3.1.0-llama` contra B = `ptbr-0.3.0-llama`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | B | 2.5 | 4.0 | 0/0 | 2/0 |
| 02-post-linkedin | B | 2.0 | 3.0 | 0/0 | 0/0 |
| 03-relatorio | B | 3.0 | 4.0 | 1/0 | 0/0 |
| 04-relatorio | B | 3.0 | 5.0 | 1/0 | 1/0 |
| 05-email-cliente | A | 4.0 | 4.0 | 0/0 | 0/0 |
| 06-email-cliente | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 07-apresentacao | B | 3.0 | 4.0 | 1/0 | 1/0 |
| 08-apresentacao | B | 3.0 | 4.0 | 1/0 | 0/0 |
| 09-resposta-chat | A | 4.0 | 3.5 | 4/0 | 2/0 |
| 10-resposta-chat | A | 4.5 | 4.0 | 0/0 | 0/0 |
| 11-post-linkedin | B | 2.0 | 4.0 | 0/0 | 0/0 |
| 12-relatorio | B | 3.0 | 4.0 | 0/1 | 1/0 |
| controle-blumenau | B | 3.0 | 4.0 | 5/0 | 10/0 |
| controle-petrobras | B | 3.0 | 4.0 | 13/0 | 9/0 |

**Resumo:** B venceu 11.0 de 14 (A 3.0). Naturalidade média A 3.07, B 3.96. Fatos perdidos A 26, B 26; inventados A 1, B 0.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": [], "inventados": []}; B {"perdidos": ["A autora coordenou a troca do sistema de ponto eletrônico.", "Os 14% de marcações com erro de turno ocorreram especificamente no primeiro mês."], "inventados": []}

**03-relatorio**: A {"perdidos": ["A estimativa de perda de 6% das vendas foi feita pela loja."], "inventados": []}; B {"perdidos": [], "inventados": []}

**04-relatorio**: A {"perdidos": ["A reunião definiu/decidiu o adiamento da troca do ERP."], "inventados": []}; B {"perdidos": ["Que a reunião definiu/decidiu o adiamento da troca do ERP."], "inventados": []}

**07-apresentacao**: A {"perdidos": ["O parque está associado à Mata Atlântica."], "inventados": []}; B {"perdidos": ["O parque está associado à Mata Atlântica / abriga áreas de Mata Atlântica."], "inventados": []}

**08-apresentacao**: A {"perdidos": ["Controle do saldo financeiro"], "inventados": []}; B {"perdidos": [], "inventados": []}

**09-resposta-chat**: A {"perdidos": ["CPF como exemplo de dado coletado", "telefone como exemplo de dado coletado", "emissão de nota fiscal como exemplo de uso dos dados", "atendimento como exemplo de uso dos dados"], "inventados": []}; B {"perdidos": ["Uso dos dados para emissão de nota fiscal.", "Uso dos dados para atendimento."], "inventados": []}

**12-relatorio**: A {"perdidos": [], "inventados": ["38% dos contatos eram a maioria dos contatos."]}; B {"perdidos": ["A automação pode reduzir o volume de atendimentos manuais."], "inventados": []}

**controle-blumenau**: A {"perdidos": ["Hermann Bruno Otto Blumenau também era farmacêutico.", "Hermann Bruno Otto Blumenau chegou em um barco, via rio Itajaí-Açu.", "Ele desembarcou à foz do ribeirão Garcia.", "O Stammtisch ocorre na rua XV de Novembro, no Centro do município.", "As outras manifestações mencionadas são das culturas europeia e brasileira."], "inventados": []}; B {"perdidos": ["Blumenau localiza-se na microrregião homônima.", "Blumenau localiza-se na Mesorregião do Vale do Itajaí.", "Hermann Bruno Otto Blumenau também era farmacêutico.", "Hermann Bruno Otto Blumenau chegou em um barco pelo rio Itajaí-Açu.", "Os dezessete colonos que acompanharam Hermann Bruno Otto Blumenau eram seus compatriotas.", "A agenda cultural destaca a colonização alemã.", "A Oktoberfest acontece todos os anos.", "O Stammtisch ocorre na rua XV de Novembro, no Centro do município.", "O Centro de Tradições Gaúchas é identificado pela sigla CTG.", "As outras manifestações mencionadas são das culturas europeia e brasileira."], "inventados": []}

**controle-petrobras**: A {"perdidos": ["A Petrobras também é uma sociedade anônima.", "Por ter o Governo do Brasil como acionista majoritário, a Petrobras é uma empresa estatal de economia mista.", "O acionista majoritário é a União.", "O nome Petrobras é pronunciado “Petrobrás”.", "A produção diária de mais de 2 milhões de barris equivale a 320 mil metros cúbicos.", "Em 2011, a Petrobras estava especificamente em quinto lugar na classificação das maiores petrolíferas de capital aberto do mundo.", "Em setembro de 2010, a Petrobras passou a ser a segunda maior empresa de energia do mundo em valor de mercado.", "A informação de que a Petrobras passou a ser a segunda maior empresa de energia do mundo em setembro de 2010 vinha de dados da Bloomberg e da Agência Brasil.", "A capitalização de 72,8 bilhões de dólares equivalia, à época, a 127,4 bilhões de reais.", "A capitalização da Petrobras foi praticamente o dobro do recorde anterior.", "O recorde anterior de capitalização em capital aberto era da Nippon Telegraph and Telephone (NTT).", "O recorde anterior da NTT foi de 36,8 bilhões de dólares.", "O recorde anterior da NTT ocorreu em novembro de 1987."], "inventados": []}; B {"perdidos": ["A Petrobras é uma empresa de capital aberto, isto é, uma sociedade anônima.", "A pronúncia indicada no original é “Petrobrás”.", "O lema atual citado é: “Uma empresa integrada de energia que atua com responsabilidade social e ambiental”.", "No Forbes Global 2000 de 2020, a Petrobras foi classificada como a 70ª maior empresa pública do mundo.", "Em setembro de 2010, a Petrobras passou a ser a segunda maior empresa de energia do mundo em valor de mercado.", "A informação sobre a Petrobras ser a segunda maior empresa de energia do mundo em setembro de 2010 é atribuída a dados da Bloomberg e da Agência Brasil.", "Em setembro de 2010, a capitalização tornou a empresa conhecida internacionalmente.", "O recorde anterior de capitalização era da Nippon Telegraph and Telephone (NTT), com 36,8 bilhões de dólares em novembro de 1987.", "Em 2011, a Petrobras estava exatamente no quinto lugar na classificação das maiores petrolíferas de capital aberto do mundo."], "inventados": []}

