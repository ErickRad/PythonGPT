import requests
from langcodes import Language

def detect_language(text):
    # Define a URL e os parâmetros da solicitação para o Google Tradutor
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": "en",
        "dt": "t",
        "q": text
    }

    # Faz a solicitação GET para o Google Tradutor
    response = requests.get(url, params=params)

    # Verifica se a solicitação foi bem-sucedida e obtém o idioma detectado
    if response.status_code == 200:
        detected_language_code = response.json()[2]
        detected_language_name = Language.make(detected_language_code).display_name()
        return detected_language_name
    else:
        print("Erro ao detectar idioma. Código de status:", response.status_code)
        return None

# Exemplo de uso:
text = "Bonjour, comment ça va?"
detected_language = detect_language(text)
print("Texto:", text)
print("Idioma detectado:", detected_language)
