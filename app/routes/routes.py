from flask import Blueprint, url_for, render_template
from app.controllers.index_controller import list_doctors               # Traigo la lista del controlador.

global_scope = Blueprint("views", __name__)                             # La carpeta views posee los ficheros estáticos

@global_scope.route("/", methods=['GET'])
def index():

    return render_template("index.html", list_doctors=list_doctors)     # Se renderiza la plantilla y le paso como argumento la lista 