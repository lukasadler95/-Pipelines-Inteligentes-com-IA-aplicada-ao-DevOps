import os
import sys
import requests

def ask_ai(prompt_message):
    api_key = os.getenv("IA_API_KEY")
    if not api_key:
        print("❌ Erro: A variável de ambiente IA_API_KEY não foi configurada nos Secrets.")
        sys.exit(1)
        
    # Exemplo utilizando a estrutura da API do Google Gemini
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt_message}]
        }],
        "generationConfig": {
            "responseMimeType": "application/json" # Obriga o modelo a retornar JSON válido
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        res_json = response.json()
        # Retorna o texto bruto de dentro do payload do Gemini
        return res_json['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        print(f"❌ Falha de comunicação com a API de IA: {e}")
        sys.exit(1)