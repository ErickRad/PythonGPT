import requests

def translate_to_portuguese(text):

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": "pt",
        "dt": "t",
        "q": text
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        translation = response.json()[0][0][0]
        return translation
    else:
        print("Erro ao traduzir texto. Código de status:", response.status_code)
        return None

# Exemplo de uso:
english_text = input(": ")
portuguese_text = translate_to_portuguese(english_text)
print(portuguese_text)
