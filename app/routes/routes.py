from flask import Blueprint, url_for, render_template
from app.controllers.index_controller import view_doctors, view_clinics                                 # Traigo la listas capturada desde el controlador.
from app.controllers.admin_controller import view_doctors, view_users, view_healthCoverage, view_clinics

global_scope = Blueprint("views", __name__)                                                             # La carpeta views posee los ficheros estáticos

@global_scope.route("/", methods=['GET'])
def view_home():
    list_doctors = view_doctors()
    list_clinics = view_clinics()

    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics)          # Se renderiza la plantilla y le paso como argumento la lista 

@global_scope.route("/admin.html", methods=['GET'])
def view_admin():
    list_adminDoctors = view_doctors()
    list_adminUsers = view_users()
    list_healthCoverage = view_healthCoverage()

    list_adminClinics = view_clinics()
    data_admin = [list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics]
    # print(data_admin[0])
    # print("CERO")
    print(data_admin[1][1])
    for user in data_admin[1]:
        print(user["_id"])
    # print("UNO")
    # print(data_admin[2])
    # print("DOS")
    # print(data_admin[3])
    # print("TRES")

    return render_template("admin.html", data_admin=data_admin)          