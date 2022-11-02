from flask import Blueprint, url_for, render_template
from app.controllers.index_controller import list_doctors, list_clinics                                 # Traigo la listas capturada desde el controlador.

global_scope = Blueprint("views", __name__)                                                             # La carpeta views posee los ficheros estáticos

@global_scope.route("/", methods=['GET'])
def view_home():

    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics)          # Se renderiza la plantilla y le paso como argumento la lista 