import os
import sys
import json
from ai_client import ask_ai

def main():
    # Caminho do relatório gerado pelo pytest-cov
    cov_file = "coverage.json"
    if not os.path.exists(cov_file):
        print("❌ Relatório de cobertura não encontrado.")
        sys.exit(1)
        
    with open(cov_file, "r") as f:
        coverage_data = json.load(f)
        
    # Extrai o resumo da cobertura total
    total_coverage = coverage_data.get("totals", {}).get("percent_covered", 0)
    
    prompt = f"""
    Você é o Agente de Testes da SmartShop Cloud. Analise os dados de cobertura de código abaixo:
    - Cobertura Total: {total_coverage}%
    - Detalhes do JSON: {json.dumps(coverage_data)[:1000]} (resumo)
    
    Regra de negócio: Se a cobertura for menor que 80%, você DEVE bloquear.
    Responda RIGOROSAMENTE no formato JSON:
    {{
        "decision": "APROVADO" ou "BLOQUEADO",
        "reason": "Sua justificativa aqui baseada nas métricas"
    }}
    """
    
    ai_response = ask_ai(prompt)
    
    try:
        decision_json = json.loads(ai_response)
        print(f"\n=== DECISÃO DO AGENTE DE TESTES ===")
        print(f"Status: {decision_json['decision']}")
        print(f"Motivo: {decision_json['reason']}\n")
        
        if decision_json['decision'] == "BLOQUEADO":
            print("❌ Pipeline interrompido por baixa qualidade técnica.")
            sys.exit(1)
        else:
            print("✅ Quality Gate aprovado!")
    except Exception as e:
        print(f"Erro ao processar resposta da IA: {e}. Resposta bruta: {ai_response}")
        sys.exit(1)

if __name__ == "__main__":
    main()