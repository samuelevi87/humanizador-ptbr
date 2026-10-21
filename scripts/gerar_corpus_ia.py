"""
gerar_corpus_ia.py

Gera o corpus de textos de IA em português do Brasil via Amazon Bedrock
(Converse API), sem nenhuma instrução de estilo, para medir os tiques que
cada modelo produz por padrão.

Cada combinação modelo × gênero × tema vira um arquivo em
corpus/ia/<modelo>/<genero>-NN.md, com cabeçalho em comentário HTML
registrando modelo, prompt e data (o contador ignora comentários).

Só faz chamadas de inferência; não cria recurso na AWS.

Uso:
  python scripts/gerar_corpus_ia.py --perfil 024848461026_IADevPocAccess \
      --modelo claude=us.anthropic.claude-sonnet-4-5-20250929-v1:0 \
      --modelo nova=us.amazon.nova-pro-v1:0
  (--modelo pode repetir; o nome antes do "=" vira o nome da subpasta)
"""
import argparse
import datetime
import time
from pathlib import Path

import boto3

DESTINO = Path(__file__).resolve().parent.parent / "corpus" / "ia"

# Prompts curtos e neutros, como um usuário comum pediria. Nenhuma instrução de
# estilo, tom ou formatação: o objetivo é capturar o comportamento padrão.
# Os temas espelham artigos do corpus humano para comparar conteúdo parecido.
GENEROS = {
    "post-linkedin": [
        "Escreva um post para o LinkedIn sobre o que aprendi migrando os sistemas da minha empresa para computação em nuvem.",
        "Escreva um post para o LinkedIn sobre como o aprendizado de máquina está mudando o atendimento ao cliente.",
    ],
    "relatorio": [
        "Escreva um relatório técnico curto sobre a adoção de Linux em servidores de uma empresa de médio porte.",
        "Escreva um relatório resumindo os resultados de um projeto piloto de chatbot para atendimento em um e-commerce.",
    ],
    "email-cliente": [
        "Escreva um e-mail para um cliente explicando que a entrega do projeto vai atrasar duas semanas por causa de uma integração com o ERP.",
        "Escreva um e-mail para um cliente apresentando a proposta de um agente de IA para responder dúvidas sobre produtos.",
    ],
    "apresentacao": [
        "Escreva um texto de apresentação sobre a cidade de Blumenau.",
        "Escreva um texto de apresentação sobre a história da Embraer.",
    ],
    "resposta-chat": [
        "O que é o Plano Real e por que ele foi importante?",
        "Explique o que é a linguagem Python e para que ela serve.",
    ],
}


def gerar(cliente, modelo_id: str, prompt: str) -> str:
    """Chama a Converse API com um único turno de usuário e devolve o texto da resposta.

    Usa temperatura 0,7; modelos que recusam o parâmetro (ex.: GPT-5.x) são
    chamados de novo com a temperatura padrão deles.
    """
    mensagens = [{"role": "user", "content": [{"text": prompt}]}]
    try:
        resp = cliente.converse(modelId=modelo_id, messages=mensagens,
                                inferenceConfig={"maxTokens": 1500, "temperature": 0.7})
    except cliente.exceptions.ValidationException as erro:
        if "temperature" not in str(erro):
            raise
        resp = cliente.converse(modelId=modelo_id, messages=mensagens, inferenceConfig={"maxTokens": 1500})
    # Modelos de raciocínio podem devolver blocos sem "text" (ex.: reasoningContent)
    return "".join(b.get("text", "") for b in resp["output"]["message"]["content"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfil", required=True, help="perfil AWS (SSO) com acesso ao Bedrock")
    ap.add_argument("--regiao", default="us-east-1")
    ap.add_argument("--modelo", action="append", required=True, help="nome=modelId (repetível)")
    args = ap.parse_args()

    cliente = boto3.Session(profile_name=args.perfil, region_name=args.regiao).client("bedrock-runtime")
    hoje = datetime.date.today().isoformat()

    for par in args.modelo:
        nome, modelo_id = par.split("=", 1)
        pasta = DESTINO / nome
        pasta.mkdir(parents=True, exist_ok=True)
        for genero, prompts in GENEROS.items():
            for i, prompt in enumerate(prompts, start=1):
                arquivo = pasta / f"{genero}-{i:02d}.md"
                if arquivo.exists():  # reexecução não gasta chamada de novo
                    continue
                try:
                    texto = gerar(cliente, modelo_id, prompt)
                except Exception as erro:  # um modelo com problema não deve parar o lote
                    print(f"  erro {nome}/{genero}-{i:02d}: {erro}")
                    continue
                cabecalho = f"<!-- modelo: {modelo_id}\n     data: {hoje}\n     prompt: {prompt} -->\n\n"
                arquivo.write_text(cabecalho + texto.strip() + "\n", encoding="utf-8")
                print(f"  ok {nome}/{arquivo.name} ({len(texto.split())} palavras)")
                time.sleep(1)  # evita throttling em contas com cota baixa
