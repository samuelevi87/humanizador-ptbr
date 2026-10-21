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
        # Pedidos 03 a 06 de cada gênero: temas variados, longe de tecnologia e atendimento,
        # para que a descoberta de n-gramas separe hábito de escrita de assunto.
        "Escreva um post para o LinkedIn sobre minha volta ao trabalho depois da licença-paternidade.",
        "Escreva um post para o LinkedIn sobre o que aprendi gerenciando uma padaria familiar por dez anos.",
        "Escreva um post para o LinkedIn comemorando cinco anos de empresa.",
        "Escreva um post para o LinkedIn sobre uma demissão que mudou minha carreira.",
    ],
    "relatorio": [
        "Escreva um relatório técnico curto sobre a adoção de Linux em servidores de uma empresa de médio porte.",
        "Escreva um relatório resumindo os resultados de um projeto piloto de chatbot para atendimento em um e-commerce.",
        "Escreva um relatório sobre o consumo de energia de uma fábrica de móveis no último ano.",
        "Escreva um relatório sobre a evasão de alunos num curso técnico de enfermagem.",
        "Escreva um relatório sobre a vistoria de um prédio residencial de 1985.",
        "Escreva um relatório sobre as vendas de uma rede de farmácias no primeiro semestre.",
    ],
    "email-cliente": [
        "Escreva um e-mail para um cliente explicando que a entrega do projeto vai atrasar duas semanas por causa de uma integração com o ERP.",
        "Escreva um e-mail para um cliente apresentando a proposta de um agente de IA para responder dúvidas sobre produtos.",
        "Escreva um e-mail para um cliente cobrando uma fatura vencida há 30 dias.",
        "Escreva um e-mail para um fornecedor reclamando de um lote de tecido com defeito.",
        "Escreva um e-mail para um cliente confirmando a reserva de um salão de festas.",
        "Escreva um e-mail para um paciente remarcando uma consulta odontológica.",
    ],
    "apresentacao": [
        "Escreva um texto de apresentação sobre a cidade de Blumenau.",
        "Escreva um texto de apresentação sobre a história da Embraer.",
        "Escreva um texto de apresentação sobre o café produzido no sul de Minas Gerais.",
        "Escreva um texto de apresentação sobre a obra de Clarice Lispector.",
        "Escreva um texto de apresentação sobre a Floresta Amazônica.",
        "Escreva um texto de apresentação sobre o arquiteto Oscar Niemeyer.",
    ],
    "resposta-chat": [
        "O que é o Plano Real e por que ele foi importante?",
        "Explique o que é a linguagem Python e para que ela serve.",
        "Quem foi Santos Dumont?",
        "Como funciona a Petrobras e quem é dono dela?",
        "Por que a Copa do Mundo de 2014 foi polêmica no Brasil?",
        "Qual a diferença entre um MEI e uma microempresa?",
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
