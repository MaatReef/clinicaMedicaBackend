from flask import Blueprint, url_for, render_template, redirect
from app.controllers.index_controller import view_doctors, view_clinics                                 # Traigo la listas capturada desde el controlador.
from app.controllers.admin_controller import *

global_scope = Blueprint("views", __name__)                                                             # La carpeta views posee los ficheros estáticos

@global_scope.route("/", methods=['GET'])
def view_home():
    list_doctors = view_doctors()
    list_clinics = view_clinics()

    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics)          # Se renderiza la plantilla y le paso como argumento la lista 

@global_scope.route("/admin", methods=['GET'])
def view_admin():
    list_adminDoctors = view_doctors()
    list_adminUsers = view_users()
    list_healthCoverage = view_healthCoverage()
    list_adminClinics = view_clinics()
    data_admin = [list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics]

    return render_template("admin.html", data_admin=data_admin)          

@global_scope.route("/appointment", methods=['GET'])
def view_appointment():
    return render_template("appointment.html")

@global_scope.route("/portal", methods=['GET'])
def view_portal():
    return render_template("portal.html")

# delete 
@global_scope.route('/delete_doctor/<dni>')
def delete_doctor(dni):
    delete = delete_doctorAdmin(dni)
    return redirect(url_for("views.view_admin"))
    
@global_scope.route('/delete_clinic/<id>')
def delete_clinic(id):
    delete = delete_clinicAdmin(id)
    return redirect(url_for("views.view_admin"))
    
@global_scope.route('/delete_coverage/<id>')
def delete_coverage(id):
    delete = delete_coverageAdmin(id)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/delete_user/<dni>')
def delete_user(dni):
    delete = delete_userAdmin(dni)
    return redirect(url_for("views.view_admin"))
