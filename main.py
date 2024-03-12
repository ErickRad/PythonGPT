from flet import * #type: ignore
import wikipedia
import time

wikipedia.set_lang('pt')

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
        pesquisa = str(tf_user.value).split()
        resposta = "_".join(pesquisa)
        try:
            resposta = wikipedia.summary(
                tf_user.value, 
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

    page.add(
        Container(
            Column(
                controls=[
                    tf_user, send_button, tf_bot                   
                ]
            ),
            alignment=alignment.top_center
        )
    )

app(target=mainPage)