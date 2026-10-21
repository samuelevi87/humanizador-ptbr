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


# Conjunto de validação: separado do de teste e nunca usado para ajustar a skill.
# Só entra na decisão final de versão, para medir sobreajuste ao conjunto de teste.
FICHAS_VALIDACAO = [
    ("post-linkedin", "Escreva um post para o LinkedIn contando esta experiência.", [
        "A autora coordenou a troca do sistema de ponto eletrônico de uma fábrica com 900 funcionários.",
        "A implantação levou 3 meses.",
        "No primeiro mês, 14% das marcações vieram com erro de turno.",
        "O erro caiu para 2% depois que os supervisores passaram a revisar as marcações toda sexta-feira.",
    ]),
    ("post-linkedin", "Escreva um post para o LinkedIn sobre isto.", [
        "O autor deu aula de lógica de programação para uma turma de 32 adolescentes num curso técnico.",
        "Ele trocou as provas escritas por pequenos projetos em dupla.",
        "A reprovação caiu de 9 para 3 alunos no semestre seguinte.",
    ]),
    ("relatorio", "Escreva um relatório técnico curto com estas informações.", [
        "O tempo de resposta do site de uma loja subiu de 1,2 para 4,8 segundos na Black Friday.",
        "A causa foi uma consulta ao banco sem índice na página de busca.",
        "Criar o índice levou o tempo de resposta de volta para 1,4 segundo.",
        "A loja estima ter perdido 6% das vendas nas duas horas de lentidão.",
    ]),
    ("relatorio", "Escreva o resumo desta reunião.", [
        "A reunião decidiu adiar a troca do ERP para março de 2027.",
        "O motivo é o fechamento fiscal de dezembro.",
        "A responsável pelo cronograma é a gerente financeira, Lúcia Ramos.",
        "O orçamento aprovado foi de R$ 480 mil.",
    ]),
    ("email-cliente", "Escreva um e-mail para o cliente com estas informações.", [
        "O certificado digital do cliente vence em 15 de dezembro.",
        "Sem ele, a emissão de notas fiscais para.",
        "A renovação custa R$ 289 e leva até 5 dias úteis.",
    ]),
    ("email-cliente", "Escreva um e-mail respondendo ao cliente.", [
        "O cliente pediu desconto de 20% no contrato anual.",
        "A empresa pode dar 10% se o pagamento for à vista.",
        "A proposta vale até 30 de novembro.",
    ]),
    ("apresentacao", "Escreva um texto de apresentação deste lugar para um site de turismo.", [
        "O Parque das Nascentes fica em Blumenau.",
        "Tem trilhas de 2 a 7 quilômetros.",
        "A entrada custa R$ 30 e o parque fecha às segundas-feiras.",
        "Abriga cachoeiras e áreas de Mata Atlântica.",
    ]),
    ("apresentacao", "Escreva a descrição deste curso para a página de inscrição.", [
        "O curso se chama Excel para Pequenos Negócios.",
        "Tem 16 horas, divididas em 4 sábados.",
        "Ensina fluxo de caixa, controle de estoque e precificação.",
        "Custa R$ 390 e tem 20 vagas.",
    ]),
    ("resposta-chat", "Responda à pergunta do usuário usando estas informações.", [
        "Pergunta do usuário: o que é LGPD e o que muda para uma loja virtual pequena?",
        "LGPD é a Lei Geral de Proteção de Dados, em vigor desde 2020.",
        "A loja precisa dizer quais dados coleta e para quê.",
        "O cliente pode pedir para apagar os dados dele.",
        "A multa pode chegar a 2% do faturamento, limitada a R$ 50 milhões por infração.",
    ]),
    ("resposta-chat", "Responda à pergunta do usuário usando estas informações.", [
        "Pergunta do usuário: vale a pena usar banco vetorial para um catálogo de 300 produtos?",
        "Para 300 produtos, uma busca por palavra-chave com filtros costuma bastar.",
        "Banco vetorial ajuda quando a pessoa descreve o que quer com palavras diferentes das do catálogo.",
        "Dá para começar sem banco vetorial e medir quantas buscas ficam sem resultado.",
    ]),
    ("post-linkedin", "Escreva um post de LinkedIn anunciando isto.", [
        "O autor foi palestrante num evento de indústria em Joinville.",
        "A palestra foi sobre uso de IA no atendimento a distribuidores.",
        "Cerca de 150 pessoas assistiram.",
    ]),
    ("relatorio", "Escreva um relatório resumindo esta análise.", [
        "Foram analisadas 1.200 conversas de atendimento por WhatsApp de setembro.",
        "38% das conversas eram sobre segunda via de boleto.",
        "O tempo médio de primeira resposta foi de 47 minutos.",
        "A recomendação é automatizar a segunda via de boleto.",
    ]),
]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfil", required=True)
    ap.add_argument("--regiao", default="us-east-1")
    ap.add_argument("--modelo", required=True, help="modelId do Bedrock usado para escrever os textos")
    ap.add_argument("--conjunto", choices=["teste", "validacao"], default="teste")
    args = ap.parse_args()

    cliente = boto3.Session(profile_name=args.perfil, region_name=args.regiao).client("bedrock-runtime")
    destino = DESTINO.parent / args.conjunto
    destino.mkdir(parents=True, exist_ok=True)
    hoje = datetime.date.today().isoformat()
    fichas = FICHAS if args.conjunto == "teste" else FICHAS_VALIDACAO

    for n, (genero, pedido, fatos) in enumerate(fichas, start=1):
        base = destino / f"{n:02d}-{genero}"
        if base.with_suffix(".md").exists():  # reexecução não gasta chamada de novo
            continue
        prompt = pedido + "\n\n" + "\n".join(f"- {f}" for f in fatos)
        texto = gerar(cliente, args.modelo, prompt).strip()
        base.with_suffix(".md").write_text(
            f"<!-- modelo: {args.modelo}\n     data: {hoje}\n     pedido: {pedido} -->\n\n{texto}\n", encoding="utf-8")
        base.with_name(base.name + ".fatos.md").write_text(
            "# Fatos que a reescrita precisa preservar\n\n" + "\n".join(f"- {f}" for f in fatos) + "\n", encoding="utf-8")
        print(f"  ok {base.name} ({len(texto.split())} palavras)")
