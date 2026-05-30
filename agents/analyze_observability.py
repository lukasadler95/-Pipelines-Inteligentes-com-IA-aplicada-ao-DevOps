import os
import json
import subprocess
from ai_client import ask_ai

def create_github_issue(title, body):
    """Utiliza a CLI do GitHub embutida no Actions para criar uma issue"""
    try:
        subprocess.run([
            "gh", "issue", "create", 
            "--title", title, 
            "--body", body, 
            "--label", "incidente-ia"
        ], check=True)
        print(f"⚠️ GitHub Issue criada para: {title}")
    except Exception as e:
        print(f"Erro ao criar issue via GitHub CLI: {e}")

def main():
    # 1. Ler Logs
    with open("logs/app.log", "r") as f:
        logs = f.read()

    # 2. Ler Métricas
    with open("metrics/system_metrics.json", "r") as f:
        metrics = json.load(f)

    # 3. Ler Traces
    with open("traces/distributed_trace.json", "r") as f:
        traces = json.load(f)

    prompt = f"""
    Você é o Especialista em Observabilidade da SmartShop Cloud. Analise os três insumos do sistema:
    
    LOGS:
    {logs}
    
    MÉTRICAS:
    {json.dumps(metrics)}
    
    TRACES:
    {json.dumps(traces)}
    
    Analise erros críticos, degradação de hardware (CPU/Latência) e gargalos de serviços.
    Responda em formato JSON com o seguinte padrão:
    {{
        "alert_required": true ou false,
        "issue_title": "Título resumido do problema encontrado",
        "diagnose": "Análise detalhada contendo o serviço problemático apontado no trace, métricas estouradas e os erros do log."
    }}
    """
    
    response = ask_ai(prompt)
    
    try:
        result = json.loads(response)
        if result.get("alert_required"):
            print("🚨 Anomalia Detectada pela IA!")
            create_github_issue(result["issue_title"], result["diagnose"])
        else:
            print("✅ Sistema operando dentro dos parâmetros normais.")
    except Exception as e:
        print(f"Erro ao processar resposta: {e}")

if __name__ == "__main__":
    main()