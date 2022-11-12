from flask import Blueprint, url_for, render_template, redirect, request
from app.controllers.index_controller import view_doctors, view_clinics                                 # Traigo la listas capturada desde el controlador.
from app.controllers.admin_controller import *

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

    return render_template("admin.html", data_admin=data_admin)          

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
    
# edit
@global_scope.route('/edit_coverage', methods=['GET', 'POST'])
def edit_coverage():
    if request.method == 'POST':
        _id = request.form['_id']
        id = request.form['id']
        name = request.form['name']
        plan = request.form['plan']
        logo = request.form['logo']
        list_coverage = [_id, id, name, plan, logo]
        list_complet = edit_coverageAdmin(list_coverage)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    if request.method == 'POST':
        _id = request.form['_id']
        avatar = request.form['avatar']
        dni = request.form['dni']
        name = request.form['name']
        healthCoverage = request.form['healthCoverage']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        active = request.form['active']
        list_user = [_id, avatar, dni, name, healthCoverage, email, phone, city, active]
        list_complet = edit_userAdmin(list_user)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/edit_doctor', methods=['GET', 'POST'])
def edit_doctor():
    if request.method == 'POST':
        _id = request.form['_id']
        dni = request.form['dni']
        name = request.form['name']
        speciality = request.form['speciality']
        email = request.form['email']
        city = request.form['city']
        scheduleAttention = request.form['scheduleAttention']
        active = request.form['active']
        list_doctor = [_id, dni, name, speciality, email, city, scheduleAttention, active]
        list_complet = edit_doctorAdmin(list_doctor)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/edit_clinic', methods=['GET', 'POST'])
def edit_clinic():
    if request.method == 'POST':
        _id = request.form['_id']
        name = request.form['name']
        scheduleAttention = request.form['scheduleAttention']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        list_clinic = [_id, name, scheduleAttention, email, phone, city]
        list_complet = edit_clinicAdmin(list_clinic)
    return redirect(url_for("views.view_admin"))