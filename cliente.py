import requests

# Configuração do proxy
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

try:
    # O parâmetro verify=False é comum ao usar proxies como Burp Suite 
    # para evitar erros de certificado SSL.
    response = requests.get('https://www.google.com', proxies=proxies, verify=False)
    
    print(f"Status Code: {response.status_code}")
    print(response.text[:200]) # Imprime os primeiros 200 caracteres
except Exception as e:
    print(f"Erro ao conectar: {e}")
