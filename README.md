# 🛒 SmartShop Cloud — Pipelines Inteligentes com IA aplicada ao DevOps

Este repositório contém o projeto prático de automação de esteiras CI/CD e monitoramento inteligente para a startup fictícia **SmartShop Cloud**, desenvolvido para a disciplina de DevOps na **PUCPR**. O foco principal é substituir validações tradicionais por tomadas de decisão autônomas orientadas a modelos de inteligência artificial (IA Generativa via API do Google Gemini).

---

## 🎯 Objetivo do Projeto

O objetivo do projeto é implementar o conceito de **AIOps (Inteligência Artificial para Operações de TI)** no ciclo de vida de desenvolvimento do sistema SmartShop Cloud. Em vez de utilizar regras estáticas ou limites fixos (hardcoded), o ecossistema utiliza agentes baseados em IA para analisar de forma contextualizada a qualidade do código fonte, interpretar a telemetria do ambiente produtivo e auditar vulnerabilidades críticas de segurança, agindo automaticamente no fluxo para proteger o ambiente.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Base:** Python 3.10+
* **Orquestração de Automações:** GitHub Actions
* **Inteligência Artificial:** API do Google Gemini (`gemini-2.5-flash`)
* **Framework de Testes & Cobertura:** `pytest` & `pytest-cov`
* **Gerenciamento de Incidentes:** GitHub CLI (`gh` utility integrado)
* **Modelagem de Dados:** JSON Estruturado para comunicação bi-direcional com a IA

---

## 🚀 Descrição dos Pipelines

### 1. Quality Gate com IA (`quality_gate.yml`)
Este pipeline intercepta cada `push` ou `pull_request`. Ele roda a suite de testes unitários da aplicação e gera um relatório detalhado de cobertura de código. O agente de IA lê o relatório gerado. Se a cobertura for inferior a 80% ou se arquivos críticos estiverem descobertos, a IA toma a decisão de **BLOQUEAR**, forçando o encerramento do pipeline com erro (`exit code 1`) e impedindo o deploy.

### 2. Observabilidade Inteligente (`observability.yml`)
Simula uma varredura periódica em produção. O script consolida dados multiplos do ecossistema: Logs de erro (`logs/app.log`), métricas brutas de uso de hardware (`metrics/system_metrics.json`) e o rastreamento distribuído de microsserviços (`traces/distributed_trace.json`). A IA correlaciona esses fatores em tempo real e, caso identifique degradação ou gargalo de componentes (como o timeout no banco ou lentidão no serviço de pagamentos), ela **cria um incidente (Issue) de forma 100% autônoma** no repositório com o diagnóstico detalhado.

### 3. Agente de Segurança Autônomo (`intelligent_agents.yml`)
Realiza uma varredura estática proativa nos arquivos do diretório `src/` em busca de falhas de segurança de alto risco, focando principalmente no vazamento de credenciais e chaves privadas expostas (*Hardcoded Secrets*). Caso detecte riscos críticos, o agente sabota a esteira para mitigar vazamentos em produção.

---

## 💻 Exemplos de Execução e Configuração

### Estrutura do Repositório Validada
A árvore de diretórios do projeto foi estruturada e padronizada para o reconhecimento correto dos runners do GitHub da seguinte forma:

```text
├── .github/
│   └── workflows/
│       ├── intelligent_agents.yml
│       ├── observability.yml
│       └── quality_gate.yml
├── agents/
│   ├── ai_client.py
│   ├── analyze_observability.py
│   ├── analyze_quality.py
│   └── security_agent.py
├── logs/
│   └── app.log
├── metrics/
│   └── system_metrics.json
├── src/
│   ├── __init__.py
│   └── core.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
└── traces/
    └── distributed_trace.json