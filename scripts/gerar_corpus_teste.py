"""
gerar_corpus_teste.py

Gera os textos de corpus/teste/, usados para avaliar as reescritas. Cada texto
nasce de uma ficha com fatos definidos de antemão: o modelo recebe os fatos e
um pedido comum, sem instrução de estilo, e escreve o texto com os tiques que
tiver. A ficha vira NN.fatos.md, que é a referência para conferir se a
reescrita perdeu ou inventou algum fato.

Os fatos são fictícios e genéricos de propósito (nenhum dado de cliente real),
para que o corpus possa ficar num repositório público.

Uso:
  python scripts/gerar_corpus_teste.py --perfil 024848461026_IADevPocAccess \
      --modelo us.anthropic.claude-sonnet-5-5
"""
import argparse
import datetime
from pathlib import Path

import boto3

from gerar_corpus_ia import gerar  # mesma chamada à Converse API, com o tratamento de temperatura

DESTINO = Path(__file__).resolve().parent.parent / "corpus" / "teste"

# Cada ficha: gênero, pedido (como um usuário comum pediria) e fatos que o texto precisa conter.
FICHAS = [
    ("post-linkedin", "Escreva um post para o LinkedIn contando esta experiência.", [
        "Uma equipe de 4 pessoas automatizou a triagem de chamados de suporte com um modelo de linguagem.",
        "O tempo médio de triagem caiu de 12 minutos para 3 minutos.",
        "O projeto levou 6 semanas.",
        "Na primeira versão, o modelo classificava errado 1 em cada 5 chamados de cobrança.",
        "A correção foi adicionar exemplos reais de chamados de cobrança ao prompt.",
    ]),
    ("post-linkedin", "Escreva um post para o LinkedIn sobre isto.", [
        "O autor trocou um pipeline de RAG por busca em catálogo estruturado.",
        "O catálogo tem 240 fichas de produto em Markdown.",
        "A taxa de respostas corretas subiu de 61% para 84% num conjunto de 50 perguntas.",
        "A busca semântica falhava quando duas fichas tinham nomes quase iguais.",
    ]),
    ("post-linkedin", "Escreva um post de LinkedIn anunciando isto.", [
        "O autor concluiu uma pós-graduação em Inteligência Artificial em outubro de 2026.",
        "O trabalho de conclusão foi sobre avaliação de agentes de atendimento.",
        "O orientador foi o professor Carlos Menezes.",
    ]),
    ("relatorio", "Escreva um relatório técnico curto com estas informações.", [
        "Uma API de pedidos começou a devolver erro 429 em 3 de setembro.",
        "O limite do fornecedor é de 60 requisições por minuto.",
        "O agente fazia até 4 chamadas por conversa, sem cache.",
        "A solução foi um cache de 5 minutos para consultas de estoque.",
        "Depois da mudança, os erros 429 caíram de 18% para menos de 1% das conversas.",
    ]),
    ("relatorio", "Escreva um relatório resumindo esta decisão de arquitetura.", [
        "A equipe precisava escolher entre DynamoDB e PostgreSQL para guardar o histórico de conversas.",
        "O volume previsto é de 30 mil conversas por mês.",
        "A consulta mais comum é buscar todas as mensagens de uma conversa pelo ID.",
        "A equipe escolheu DynamoDB porque não há consultas relacionais e o custo previsto é menor.",
        "O risco aceito é a dificuldade de fazer relatórios analíticos, que serão feitos exportando para o S3.",
    ]),
    ("relatorio", "Escreva o resumo de um teste com estes resultados.", [
        "Foram executados 64 testes num agente de atendimento.",
        "52 passaram, 7 falharam e 5 ficaram bloqueados por instabilidade do ERP.",
        "As falhas se concentraram em perguntas sobre prazo de entrega.",
        "O próximo passo é repetir os 12 testes que não passaram depois da correção do prompt.",
    ]),
    ("email-cliente", "Escreva um e-mail para o cliente com estas informações.", [
        "A entrega da fase 2 vai atrasar de 10 de novembro para 24 de novembro.",
        "O motivo é que a API do ERP do cliente ainda não liberou o endpoint de estoque.",
        "A equipe precisa de um usuário de teste com acesso a esse endpoint até 31 de outubro.",
    ]),
    ("email-cliente", "Escreva um e-mail respondendo ao cliente.", [
        "O cliente perguntou se o agente pode responder sobre preços.",
        "O agente pode responder preços, desde que a tabela seja enviada em planilha e atualizada mensalmente.",
        "Preços promocionais não entram na primeira versão.",
    ]),
    ("apresentacao", "Escreva um texto de apresentação desta empresa para o site.", [
        "A empresa se chama Tecelagem Vale Azul.",
        "Foi fundada em 1978 em Brusque, Santa Catarina.",
        "Produz tecidos de algodão para cama e banho.",
        "Tem 320 funcionários.",
        "Exporta para Uruguai e Paraguai.",
    ]),
    ("apresentacao", "Escreva uma descrição deste produto para a loja virtual.", [
        "O produto é uma garrafa térmica de aço inox de 1 litro.",
        "Mantém bebidas quentes por 12 horas e frias por 24 horas.",
        "Tem tampa com trava e alça dobrável.",
        "Custa R$ 149,90.",
    ]),
    ("resposta-chat", "Responda à pergunta do usuário usando estas informações.", [
        "Pergunta do usuário: qual a diferença entre RAG e fine-tuning?",
        "RAG busca documentos na hora da pergunta e os coloca no contexto do modelo.",
        "Fine-tuning altera os pesos do modelo com exemplos de treino.",
        "RAG é melhor quando a informação muda com frequência.",
        "Fine-tuning é melhor para ensinar formato ou estilo de resposta.",
    ]),
    ("resposta-chat", "Responda à pergunta do usuário usando estas informações.", [
        "Pergunta do usuário: vale a pena usar LangGraph ou Strands Agents na AWS?",
        "Strands Agents é um SDK da AWS, integrado nativamente ao Bedrock.",
        "LangGraph modela o agente como um grafo de estados explícito.",
        "Para quem já está na AWS, Strands costuma ter menos código de integração.",
        "LangGraph dá mais controle sobre fluxos com muitos desvios e retomadas.",
    ]),
]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfil", required=True)
    ap.add_argument("--regiao", default="us-east-1")
    ap.add_argument("--modelo", required=True, help="modelId do Bedrock usado para escrever os textos")
    args = ap.parse_args()

    cliente = boto3.Session(profile_name=args.perfil, region_name=args.regiao).client("bedrock-runtime")
    DESTINO.mkdir(parents=True, exist_ok=True)
    hoje = datetime.date.today().isoformat()

    for n, (genero, pedido, fatos) in enumerate(FICHAS, start=1):
        base = DESTINO / f"{n:02d}-{genero}"
        if base.with_suffix(".md").exists():  # reexecução não gasta chamada de novo
            continue
        prompt = pedido + "\n\n" + "\n".join(f"- {f}" for f in fatos)
        texto = gerar(cliente, args.modelo, prompt).strip()
        base.with_suffix(".md").write_text(
            f"<!-- modelo: {args.modelo}\n     data: {hoje}\n     pedido: {pedido} -->\n\n{texto}\n", encoding="utf-8")
        base.with_name(base.name + ".fatos.md").write_text(
            "# Fatos que a reescrita precisa preservar\n\n" + "\n".join(f"- {f}" for f in fatos) + "\n", encoding="utf-8")
        print(f"  ok {base.name} ({len(texto.split())} palavras)")
