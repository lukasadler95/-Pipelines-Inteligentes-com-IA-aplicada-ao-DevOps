import os
import json
import sys
from ai_client import ask_ai

def main():
    # Varre os arquivos do diretório src/ em busca de código
    code_content = ""
    src_dir = "src"
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    code_content += f"\n--- Arquivo: {file} ---\n" + f.read()

    prompt = f"""
    Você é o Agente de Segurança Autônomo da SmartShop Cloud.
    Analise o código fonte abaixo em busca de vulnerabilidades, especialmente credenciais expostas (API Keys, senhas, tokens hardcoded):
    
    {code_content}
    
    Responda estritamente no formato JSON:
    {{
        "vulnerability_detected": true ou false,
        "risk_level": "CRITICAL", "HIGH", "MEDIUM" ou "LOW",
        "report": "Relatório detalhado da sua varredura e sugestão de correção."
    }}
    """
    
    response = ask_ai(prompt)
    
    try:
        report = json.loads(response)
        print("=== RELATÓRIO DO AGENTE DE SEGURANÇA ===")
        print(f"Risco: {report['risk_level']}")
        print(f"Detalhes: {report['report']}")
        
        if report['vulnerability_detected'] and report['risk_level'] in ["CRITICAL", "HIGH"]:
            print("❌ Pipeline Bloqueado devido a vulnerabilidades graves de segurança!")
            sys.exit(1)
        else:
            print("✅ Código aprovado pelo agente de segurança.")
    except Exception as e:
        print(f"Falha na análise do agente: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()