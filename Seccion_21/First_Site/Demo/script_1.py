from flask import Flask, render_template # Flask es un framework web ligero para Python
# import justpy as jp  # JustPy es un framework web para crear aplicaciones web interactivas

app = Flask(__name__)  # Crea una instancia de la aplicación Flask configurando la carpeta de templates

@app.route("/")  # Define la ruta raíz ("/") de la aplicación web
def home():  # Define la función que se ejecutará cuando se acceda a la ruta raíz
    return render_template("home.html")  # Renderiza y devuelve el archivo HTML "home.html" como respuesta    

@app.route("/about")  # Define la ruta "/about" de la aplicación web
def about():  # Define la función que se ejecutará cuando se acceda a la ruta "/about"
    return render_template("about.html")  # Renderiza y devuelve el archivo HTML "about.html" como respuesta
if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    app.run(debug=True)  # Inicia la aplicación Flask en modo de depuración
