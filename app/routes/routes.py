from flask import Blueprint, url_for, render_template, redirect, request
from app.controllers.index_controller import view_doctors, view_clinics                                 # Traigo la listas capturada desde el controlador.
from app.controllers.admin_controller import *

global_scope = Blueprint("views", __name__)                                                             # La carpeta views posee los ficheros estáticos


# View: Las siguientes rutas se encargan de presentar la data traída desde la Base de DATOS
@global_scope.route("/", methods=['GET'])
def view_home():
    list_doctors = view_doctors()
    list_clinics = view_clinics()

    # Se renderiza la plantilla y le paso como argumento la lista
    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics, title="admin", online=True)

@global_scope.route("/admin", methods=['GET'])
def view_admin():
    list_adminDoctors = view_doctors()
    list_adminUsers = view_users()
    list_healthCoverage = view_healthCoverage()
    list_adminClinics = view_clinics()
    data_admin = [list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics]

    return render_template("admin.html", data_admin=data_admin, internalonline=True)

@global_scope.route("/appointment", methods=['GET'])
def view_appointment():
    return render_template("appointment.html")


@global_scope.route("/portal", methods=['GET'])
def view_portal():
    return render_template("portal.html")

# Delete: Las siguientes rutas se encargan de eliminar la data en la base de datos desde el formulario de la sección admin
@global_scope.route('/delete_doctor/<_id>')
def delete_doctor(_id):
    delete = delete_doctorAdmin(_id)
    return redirect(url_for("views.view_admin"))
    
@global_scope.route('/delete_clinic/<_id>' )
def delete_clinic(_id):
    delete = delete_clinicAdmin(_id)
    return redirect(url_for("views.view_admin"))
    
@global_scope.route('/delete_coverage/<_id>')
def delete_coverage(_id):
    delete = delete_coverageAdmin(_id)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/delete_user/<_id>')
def delete_user(_id):
    delete = delete_userAdmin(_id)
    return redirect(url_for("views.view_admin"))
    

# Edit: Las siguientes rutas se encargan de la edición de la data en la Base de Datos desde la sección admin
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


# Post : Las siguientes rutas se encargan de agregar data en la base de datos desde el formulario de la sección Admin
@global_scope.route('/post_doctor', methods=['GET', 'POST'])
def post_doctor():
    if request.method == 'POST':
        dni = request.form['dni']
        name = request.form['name']
        email = request.form['email']
        avatar = request.form['avatar']
        scheduleAttention = request.form['scheduleAttention']
        speciality = request.form['speciality']
        active = request.form['active']
        attention = request.form['attention']
        list_doctor = [dni, name, email, avatar, scheduleAttention, speciality, active, attention]
        list_complet = post_doctorAdmin(list_doctor)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/post_user', methods=['GET', 'POST'])
def post_user():
    if request.method == 'POST':
        avatar = request.form['avatar']
        dni = request.form['dni']
        name = request.form['name']
        healthCoverage = request.form['healthCoverage']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        active = request.form['active']
        list_user = [avatar, dni, name, healthCoverage, email, phone, city, active]
        list_complet = post_userAdmin(list_user)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/post_healthCoverage', methods=['GET', 'POST'])
def post_healthCoverage():
    if request.method == 'POST':
        logo = request.form['logo']
        name = request.form['name']
        plan = request.form['plan']
        list_healthCoverage = [logo, name, plan]
        list_complet = post_healthAdmin(list_healthCoverage)
    return redirect(url_for("views.view_admin"))

@global_scope.route('/post_clinic', methods=['GET', 'POST'])
def post_clinic():
    if request.method == 'POST':
        name = request.form['name']
        scheduleAttention = request.form['scheduleAttention']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        photo = request.form['photo']
        list_clinic = [name, scheduleAttention, email, phone, city, photo]
        list_complet = post_clinicAdmin(list_clinic)
    return redirect(url_for("views.view_admin"))