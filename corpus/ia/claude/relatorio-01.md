<!-- modelo: us.anthropic.claude-sonnet-5-5
     data: 2026-10-21
     prompt: Escreva um relatório técnico curto sobre a adoção de Linux em servidores de uma empresa de médio porte. -->

# Relatório Técnico: Adoção de Linux em Servidores Corporativos

**Empresa:** Médio porte (150 a 500 colaboradores)
**Área responsável:** Tecnologia da Informação
**Objetivo:** Avaliar a viabilidade, os benefícios, os riscos e o plano de adoção de Linux na infraestrutura de servidores

---

## 1. Resumo Executivo

Este relatório analisa a migração parcial ou total dos servidores da empresa para distribuições Linux. A análise indica que a adoção é **viável e recomendada**, com ganhos esperados em custo de licenciamento, segurança, desempenho e flexibilidade de automação. Recomenda-se uma migração **gradual, em fases**, começando por serviços de menor criticidade.

---

## 2. Cenário Atual

- Parque misto, com predominância de servidores Windows Server.
- Custos recorrentes de licenciamento (sistema operacional, CALs e bancos de dados).
- Serviços típicos: arquivos, aplicações web, banco de dados, e-mail, backup e monitoramento.
- Equipe de TI com pouca experiência em Linux, o que exige capacitação.

---

## 3. Distribuições Avaliadas

| Distribuição | Perfil | Suporte | Indicação |
|---|---|---|---|
| **Red Hat Enterprise Linux (RHEL)** | Corporativo | Comercial (pago) | Ambientes críticos, exigências de conformidade |
| **Ubuntu Server LTS** | Versátil | Comunitário e comercial (Canonical) | Aplicações web, nuvem, contêineres |
| **Debian** | Estável | Comunitário | Serviços de longa duração, baixo custo |
| **AlmaLinux / Rocky Linux** | Compatíveis com RHEL | Comunitário | Alternativa gratuita ao RHEL |

**Sugestão:** Ubuntu Server LTS ou AlmaLinux/Rocky Linux, pelo equilíbrio entre custo, estabilidade e disponibilidade de profissionais.

---

## 4. Benefícios Esperados

1. **Redução de custos:** eliminação ou redução de licenças de sistema operacional e de parte do software de infraestrutura.
2. **Segurança:** controle granular de permissões, atualizações rápidas e ferramentas como SELinux, AppArmor e iptables/nftables.
3. **Estabilidade e desempenho:** menor consumo de recursos e alta disponibilidade de uptime.
4. **Automação:** integração nativa com Bash, Ansible, Terraform e Docker.
5. **Flexibilidade:** ausência de dependência de um único fornecedor (*vendor lock-in*).
6. **Alinhamento com a nuvem:** a maior parte das cargas em AWS, Azure e Google Cloud roda em Linux.

---

## 5. Riscos e Desafios

| Risco | Impacto | Mitigação |
|---|---|---|
| Falta de qualificação da equipe | Alto | Treinamento e certificações (LPIC, RHCSA) |
| Incompatibilidade com sistemas legados | Médio | Inventário prévio, uso de virtualização ou *containers* |
| Resistência à mudança | Médio | Comunicação clara e envolvimento das equipes |
| Suporte inadequado | Médio | Contrato de suporte comercial para sistemas críticos |
| Falhas durante a migração | Alto | Testes em homologação e plano de *rollback* |

---

## 6. Plano de Adoção Proposto

**Fase 1 – Diagnóstico (1 mês)**
Inventário de servidores, aplicações e dependências; definição da distribuição padrão.

**Fase 2 – Capacitação e Piloto (2 a 3 meses)**
Treinamento da equipe e implantação em ambiente de testes com serviços de baixo risco (ex.: servidor web interno, DNS, proxy).

**Fase 3 – Migração Gradual (4 a 6 meses)**
Migração de serviços como arquivos (Samba), banco de dados (PostgreSQL/MySQL), aplicações e monitoramento (Zabbix, Prometheus).

**Fase 4 – Consolidação (contínua)**
Padron
