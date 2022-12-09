from flask import Blueprint, url_for, render_template, redirect, request, session, flash
# from flask_login import logout_user
# from werkzeug.security import generate_password_hash, check_password_hash     
# Para "hashear" contraseñas y luego comparar el hash con el tecto plano

# Traigo la listas capturada desde el controlador.
from app.controllers.index_controller import *                                  
from app.controllers.admin_controller import *
from app.models.Users import Users

# La carpeta views posee los ficheros estáticos
edit_scope = Blueprint("edit", __name__)   

# Edit: Las siguientes rutas se encargan de la edición de la data en la Base de Datos desde la sección admin
@edit_scope.route('/edit_coverage', methods=['GET', 'POST'])
def edit_coverage():
    if request.method == 'POST':
        _id = request.form['_id']
        id = request.form['id']
        name = request.form['name']
        plan = request.form['plan']
        logo = request.form['logo']
        list_coverage = [_id, id, name, plan, logo]
        list_complet = edit_coverageAdmin(list_coverage)
    return redirect(url_for("view.view_admin"))

@edit_scope.route('/edit_user', methods=['GET', 'POST'])
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
        status = request.form['status']
        password = request.form['password']
        list_user = [_id, avatar, dni, name, healthCoverage, email, phone, city, active, status, password]
        list_complet = edit_userAdmin(list_user)
    return redirect(url_for("view.view_admin"))

@edit_scope.route('/edit_doctor', methods=['GET', 'POST'])
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
    return redirect(url_for("view.view_admin"))

@edit_scope.route('/edit_clinic', methods=['GET', 'POST'])
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
    return redirect(url_for("view.view_admin"))

@edit_scope.route('/edit_appointment', methods=['GET', 'POST'])
def edit_appointment():
    if request.method == 'POST':
        user_id = request.form['user_id']
        _id = request.form['_id']
        appointmentDate = request.form['appointmentDate']
        observations = request.form['observations']
        speciality = request.form['speciality']
        modality = request.form['modality']
        appointment_form = [
            user_id, 
            _id, 
            appointmentDate,
            observations, 
            speciality, 
            modality
        ]
        new_appointment = Users.edit_userApp(appointment_form)
    return redirect(url_for("view.view_portal_appointments", _id=user_id))
