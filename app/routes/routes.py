from flask import Blueprint, url_for, render_template
from app.controllers.index_controller import list_doctors, list_clinics                                 # Traigo la listas capturada desde el controlador.
from app.controllers.admin_controller import list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics

global_scope = Blueprint("views", __name__)                                                             # La carpeta views posee los ficheros estáticos

@global_scope.route("/", methods=['GET'])
def view_home():
    
    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics)          # Se renderiza la plantilla y le paso como argumento la lista 

@global_scope.route("/admin.html", methods=['GET'])
def view_admin():
    
    data_admin = [list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics]
    return render_template("admin.html", data_admin=data_admin)          