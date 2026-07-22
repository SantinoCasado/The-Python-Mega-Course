import justpy as jp

def app():
    wp = jp.QuasarPage()  # Crea una nueva página web utilizando justpy con el tema Quasar
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")  # agrega un encabezado de nivel 1 (h1) y aplica clases CSS para el estilo
    p1 = jp.QDiv(a=wp, text = "These graphs represent course review analysis", classes="text-subtitle1 text-center q-pa-md")  # agrega un párrafo con texto descriptivo y aplica clases CSS para el estilo

    return wp

jp.justpy(app)