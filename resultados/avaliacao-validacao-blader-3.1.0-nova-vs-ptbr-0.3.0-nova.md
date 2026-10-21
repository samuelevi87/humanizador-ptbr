# Avaliação: A = `blader-3.1.0-nova` contra B = `ptbr-0.3.0-nova`

Juiz: `us.openai.gpt-5.5`. Preferência cega nas duas ordens.

| Texto | Mais humano | Nota A | Nota B | A perdidos/inventados | B perdidos/inventados |
|---|---|---|---|---|---|
| 01-post-linkedin | A | 4.0 | 3.0 | 2/0 | 1/0 |
| 02-post-linkedin | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 03-relatorio | B | 3.0 | 4.0 | 0/0 | 0/0 |
| 04-relatorio | B | 4.0 | 5.0 | 0/0 | 0/0 |
| 05-email-cliente | A | 4.5 | 3.0 | 0/0 | 0/0 |
| 06-email-cliente | A | 4.0 | 3.0 | 0/0 | 0/0 |
| 07-apresentacao | B | 2.0 | 3.0 | 0/0 | 0/0 |
| 08-apresentacao | B | 2.5 | 3.5 | 1/0 | 1/0 |
| 09-resposta-chat | empate | 3.5 | 3.5 | 0/0 | 0/0 |
| 10-resposta-chat | A | 4.5 | 3.5 | 1/0 | 0/0 |
| 11-post-linkedin | B | 2.0 | 3.0 | 1/0 | 0/0 |
| 12-relatorio | B | 2.0 | 3.0 | 0/0 | 0/0 |
| controle-blumenau | empate | 3.5 | 3.0 | 23/0 | 0/0 |
| controle-petrobras | A | 4.0 | 3.0 | 19/0 | 16/0 |

**Resumo:** B venceu 7.5 de 14 (A 6.5). Naturalidade média A 3.36, B 3.36. Fatos perdidos A 47, B 18; inventados A 0, B 0.

## Detalhe de fidelidade

**01-post-linkedin**: A {"perdidos": ["A coordenação ocorreu nos últimos meses.", "Os supervisores conhecem a operação de perto e conseguem identificar inconsistências rapidamente."], "inventados": []}; B {"perdidos": ["Os supervisores conhecem a operação de perto e conseguem identificar inconsistências rapidamente."], "inventados": []}

**08-apresentacao**: A {"perdidos": ["O curso se chama Excel para Pequenos Negócios."], "inventados": []}; B {"perdidos": ["O curso se chama Excel para Pequenos Negócios."], "inventados": []}

**10-resposta-chat**: A {"perdidos": ["Exemplo específico de busca livre: “presente para criança que gosta de montar” em vez de “blocos de construção”."], "inventados": []}; B {"perdidos": [], "inventados": []}

**11-post-linkedin**: A {"perdidos": ["A palestra ocorreu em um evento de indústria."], "inventados": []}; B {"perdidos": [], "inventados": []}

**controle-blumenau**: A {"perdidos": ["Blumenau localiza-se na Região Sul do Brasil.", "Blumenau localiza-se na microrregião homônima.", "Blumenau localiza-se na Mesorregião do Vale do Itajaí.", "Blumenau é a cidade-sede da Região Metropolitana do Vale do Itajaí.", "Blumenau é o 8º município mais populoso da Região Sul do Brasil.", "Blumenau é o 78º município mais populoso do Brasil.", "Blumenau é a única cidade média-grande de Santa Catarina.", "Hermann Bruno Otto Blumenau chegou em um barco via rio Itajaí-Açu.", "Hermann Bruno Otto Blumenau chegou acompanhado de outros dezessete colonos compatriotas.", "Hermann Bruno Otto Blumenau desembarcou à foz do ribeirão Garcia em 2 de setembro de 1850.", "Hermann Bruno Otto Blumenau dividiu a gleba em lotes para que os colonos pudessem edificar suas moradias.", "As moradias dos colonos eram majoritariamente casas feitas com a técnica enxaimel.", "O intervalo ocupado entre as fozes dos ribeirões Velha e Garcia definiu o atual centro da cidade.", "A agenda cultural é focada em festas baseadas no cotidiano e nos hábitos dos imigrantes europeus.", "Na agenda cultural, destaca-se a colonização alemã.", "A Oktoberfest é a segunda maior festa de cerveja do mundo.", "A Oktoberfest acontece todos os anos em outubro.", "A Oktoberfest acontece durante 17 dias.", "O Stammtisch é uma tradicional reunião de associações.", "O Stammtisch ocorre na rua XV de Novembro, no Centro do município.", "O Stammtisch ocorre também na Vila Itoupava.", "A Festitália é realizada pelo núcleo italiano da população.", "Também ocorrem diversas outras manifestações das culturas europeia e brasileira."], "inventados": []}; B {"perdidos": [], "inventados": []}

**controle-petrobras**: A {"perdidos": ["O nome completo “Petróleo Brasileiro S.A.” e a forma/menção “Petrobras; pronunciado Petrobrás”.", "A Petrobras é uma sociedade anônima e uma empresa estatal de economia mista.", "O acionista majoritário é o Governo do Brasil, especificado como a União.", "A sede da empresa fica no Rio de Janeiro.", "As áreas prioritárias de atuação: exploração, produção, refino, comercialização e transporte de petróleo, gás natural e seus derivados.", "O lema atual: “Uma empresa integrada de energia que atua com responsabilidade social e ambiental”.", "No Forbes Global 2000 de 2020, a Petrobras foi classificada como a 70ª maior empresa pública do mundo.", "A data exata de instituição da empresa: 3 de outubro de 1953.", "A equivalência da produção diária de mais de 2 milhões de barris a 320 mil metros cúbicos.", "A Petrobras é proprietária de refinarias e petroleiros.", "A Petrobras é uma grande distribuidora de derivados de petróleo.", "Em 2010, em valor de mercado, foi a segunda maior empresa do continente americano e a quarta maior do mundo.", "A posição de segunda maior empresa de energia do mundo em valor de mercado ocorreu em setembro de 2010.", "A informação sobre a segunda maior empresa de energia do mundo veio de dados da Bloomberg e da Agência Brasil.", "Em setembro de 2010, a empresa ficou conhecida internacionalmente pela maior capitalização em capital aberto da história.", "O valor de 72,8 bilhões de dólares equivalia, à época, a 127,4 bilhões de reais.", "A capitalização de 72,8 bilhões de dólares foi praticamente o dobro do recorde anterior.", "O recorde anterior era da Nippon Telegraph and Telephone, NTT.", "O recorde anterior havia sido de 36,8 bilhões de dólares, capitalizados em novembro de 1987."], "inventados": []}; B {"perdidos": ["O nome completo \"Petróleo Brasileiro S.A.\".", "A pronúncia \"Petrobrás\".", "A Petrobras é uma empresa estatal de economia mista.", "A sede da empresa fica no Rio de Janeiro.", "A atuação citada inclui derivados de petróleo e gás natural nas áreas de exploração, produção, refino, comercialização e transporte.", "O lema atual: \"Uma empresa integrada de energia que atua com responsabilidade social e ambiental\".", "A produção diária de mais de 2 milhões de barris corresponde a 320 mil metros cúbicos.", "A Petrobras é uma multinacional.", "Em 2011, o quinto lugar era na classificação das maiores petrolíferas de capital aberto do mundo.", "Em setembro de 2010, a Petrobras passou a ser a segunda maior empresa de energia do mundo em valor de mercado.", "A informação sobre a segunda maior empresa de energia do mundo foi atribuída à Bloomberg e à Agência Brasil.", "A capitalização de 72,8 bilhões de dólares equivalia, à época, a 127,4 bilhões de reais.", "A capitalização de 2010 foi praticamente o dobro do recorde anterior.", "O recorde anterior era da Nippon Telegraph and Telephone (NTT).", "O recorde anterior foi de 36,8 bilhões de dólares.", "O recorde anterior ocorreu em novembro de 1987."], "inventados": []}

