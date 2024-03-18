from flet import * #type: ignore
import wikipedia
import requests
import time
import pyttsx3
import nltk
import nltk.tokenize as tk

wikipedia.set_lang('pt')
voz = pyttsx3.init('sapi5')
voz.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")
voz.setProperty('rate', 230)

def translate(text, input, output):

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": input,
        "tl": output,
        "dt": "t",
        "q": text
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        translation = response.json()[0][0][0]
        return translation
    else:
        print(response.status_code)
        return None
    
    
def get_topic(frase):
    topic = []
    words = tk.word_tokenize(frase)
    tags = nltk.pos_tag(words)
    for word, tag in tags:
        if tag in ['NN', 'NNS', 'NNP', 'NNPS'] and word.lower() not in ['?', '.' , 'que', 'o', 'quem', 'foi']:
            topic.append(word)
    
    return [word for word in topic]

def mainPage(page: Page):
    page.title = "PythonGPT"

    tf_user = TextField(
        hint_text="Sobre o que você quer saber?",
        suffix_icon=icons.PERSON_OUTLINE_ROUNDED,
        border_color= colors.WHITE,
        color=colors.WHITE,
        border_radius= BorderRadius(30, 30, 30, 30)
         
    
    )
    tf_bot = TextField(
        prefix_icon=icons.BOLT,
        border_color= colors.WHITE,
        color=colors.WHITE,
        multiline=True,
        visible=False,
        border_radius= BorderRadius(30, 30, 30, 30) 
    )
    

    def clicked(x):
        tf_bot.visible = True
        pesquisa = get_topic(tf_user.value)
        try:
            resposta = wikipedia.summary(
                pesquisa, 
                sentences=3
            )

        except wikipedia.exceptions.DisambiguationError:
            resposta = "Não entendi. Você pode ser mais específico?"


        tf_bot.value = ""
        for char in resposta:
            tf_bot.value += char
            time.sleep(0.010)
            page.update()

        tf_user.value = ""
        page.update()

    def speak(x):
        voz.say(tf_bot.value)
        voz.runAndWait()

    send_button = Container(
        IconButton(
            scale=1.3,
            icon=icons.PLAY_CIRCLE_OUTLINE,
            icon_color=colors.WHITE,
            on_click=clicked,
            visible=True
        ),
        alignment=alignment.center_right
    )

    speak_button = Container(
        IconButton(
            scale=1.3,
            icon=icons.MIC,
            icon_color=colors.WHITE,
            on_click=speak,
            visible=True
        ),
        alignment=alignment.center_right
    )


    page.add(
        Container(
            Column(
                controls=[
                    tf_user, speak_button, send_button, tf_bot                   
                ]
            ),
            alignment=alignment.top_center
        )
    )

app(target=mainPage)