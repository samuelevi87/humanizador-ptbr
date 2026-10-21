# humanizador-ptbr

Skill para Claude Code (e outros agentes compatíveis com Agent Skills) que reescreve texto em português do Brasil com cara de IA para que soe como quem escreveu, sem mudar o que o texto diz.

**Antes** (gerado por IA):

> Localizado em Blumenau, o Parque das Nascentes é um convite para quem deseja se conectar com a natureza e descobrir a beleza da Mata Atlântica. O espaço abriga áreas preservadas, cachoeiras e trilhas que variam de 2 a 7 quilômetros, oferecendo opções para diferentes níveis de disposição e experiência.
>
> Ideal para caminhadas, contemplação e momentos de tranquilidade ao ar livre, o parque proporciona uma experiência imersiva em meio à vegetação nativa e aos sons da natureza. A entrada custa R$ 30, e é importante lembrar que o parque não abre às segundas-feiras.
>
> Uma ótima opção para incluir no roteiro de quem visita Blumenau e busca contato direto com paisagens naturais encantadoras.

**Depois** (humanizador-ptbr):

> O Parque das Nascentes fica em Blumenau e tem áreas preservadas de Mata Atlântica, cachoeiras e trilhas de 2 a 7 quilômetros, para quem quer um passeio curto ou uma caminhada mais longa.
>
> Dá para caminhar, descansar e ficar ao ar livre no meio da vegetação nativa. A entrada custa R$ 30. O parque não abre às segundas-feiras.
>
> Vale incluir no roteiro de quem visita Blumenau e quer ver uma paisagem natural de perto.

## Instalação

**Claude Code:**

```
/plugin marketplace add samuelevi87/humanizador-ptbr
/plugin install humanizador-ptbr@humanizador-ptbr
```

**Outros agentes** (Codex, Gemini CLI, Cursor e outros compatíveis com Agent Skills): `npx skills add samuelevi87/humanizador-ptbr --global --agent '*'`, ou copie o `SKILL.md` para a pasta de skills do agente.

## Uso

- `/humanizador-ptbr` seguido do texto: devolve o rascunho, os padrões que sobraram e a versão final.
- Indicando um arquivo: grava só a versão final e mexe só na prosa (código, YAML, comandos e links ficam intactos).
- Chamada por outra skill: devolve só a versão final.
- Para calibrar a voz, cole 2 ou 3 parágrafos seus ou crie um `voz.md` no projeto.

## Por que uma versão em português

O [Humanizer](https://github.com/blader/humanizer), de Siqi Chen, se baseia no guia [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipedia e foi escrito para inglês. Testado em português, ele vai muito bem quando quem reescreve é o Claude Sonnet, mas rende pouco com modelos menores, como Amazon Nova e Llama: eles não generalizam a partir dos exemplos em inglês. Esta versão traz o catálogo e os exemplos em português e foi pensada para funcionar também nesses modelos.

O catálogo tem 27 padrões em sete grupos. O grupo P traz tiques do português de IA que o original não cobre ("para garantir", "essencial para", "jornada", "ecossistema", "alavancar", conectores de redação). Ficaram de fora padrões que o português usa naturalmente ("possui", "realizar", voz passiva, sujeito oculto, regra de hífen do inglês).

## Como foi construído e medido

Nenhum padrão entrou por impressão pessoal. Tudo está em `corpus/`, `scripts/` e `resultados/`:

1. **Corpus:** 180 textos gerados por 6 modelos (Claude, GPT, Nova, Llama, Mistral, Gemma) sem instrução de estilo, contra 19 artigos da Wikipédia lusófona anteriores a 30/11/2022. Um padrão entra quando aparece bem mais em texto de IA (`resultados/analise-v1.md`). Os dois padrões mais fortes, placeholder (`[Nome da Empresa]`, 85 vezes mais frequente) e finalidade genérica (10 vezes), não estavam na lista inicial: vieram da descoberta por n-gramas.
2. **Avaliação:** a mesma rodada de reescrita com as duas skills, com três modelos reescritores, julgada às cegas por um modelo de outra família (GPT-5.5), nas duas ordens. Números conferidos por um verificador determinístico.
3. **Validação:** a versão final foi medida num conjunto de textos que nunca foi usado para ajustar a skill.
4. **Teste humano:** teste cego com um leitor nativo.

### Resultados da v1.0.0 (conjunto de validação)

| Reescritor | humanizador-ptbr preferido pelo juiz | Números preservados |
|---|---|---|
| Claude Sonnet 5.5 | 10,5 de 14 | 35/35 |
| Llama 4 Maverick | 11 de 14 | 35/35 |
| Amazon Nova Pro | 7,5 de 14 (empate; perdeu 18 fatos contra 47 do original) | 35/35 |

No teste cego humano (6 textos, três versões cada), a versão PT-BR foi a mais humana em 3 e nunca a pior; o Humanizer original foi o pior em 3.

## Limites conhecidos

- Em post de rede social, a skill tende a juntar parágrafos curtos, e o leitor preferiu o ritmo original com parágrafos curtos mesmo quando o texto tinha tiques.
- Às vezes formaliza o que já era natural ("Obrigado" vira "Agradecemos").
- Em texto sem sinais de IA, ainda mexe mais do que deveria com modelos menores (o original tem o mesmo problema).
- O controle humano do corpus é só enciclopédico: padrões de e-mail e de segunda pessoa não foram validados por frequência.
- O juiz LLM e o leitor humano concordaram pouco (1 de 4 casos comparáveis). O juiz serve para detectar regressão entre versões, não para dizer o que um leitor prefere.

## Licença e crédito

MIT. Mantém o aviso de copyright do Humanizer original. Os textos em `corpus/humano/wikipedia/` são da Wikipédia, sob CC BY-SA 4.0, com atribuição no cabeçalho de cada arquivo.
