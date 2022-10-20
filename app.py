# Hacemos la instancia de nuestro Framework
from flask import Flask, url_for, render_template

# Acá hacemos referencia al archivo que estamos manipulando
app = Flask(__name__)

# Decorador @, expande las funciones de una función
@app.route("/")
def index():
    #Importamos el render desde Flask y le pasamos el archivo que se encuentra en la carpeta templates
    return render_template("index.html")
