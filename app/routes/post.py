from flask import Blueprint, url_for, render_template, redirect, request, session, flash
# from flask_login import logout_user
# from werkzeug.security import generate_password_hash, check_password_hash     
# Para "hashear" contraseñas y luego comparar el hash con el tecto plano

# Traigo la listas capturada desde el controlador.
from app.controllers.index_controller import *                                  
from app.controllers.admin_controller import *
from app import login_manager
from flask_login import login_user, login_required, logout_user, current_user


# La carpeta views posee los ficheros estáticos
post_scope = Blueprint("post", __name__)   

# Post : Las siguientes rutas se encargan de agregar data en la base de datos desde el formulario de la sección Admin
@post_scope.route('/post_doctor', methods=['GET', 'POST'])
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
    return redirect(url_for("view.view_admin"))

@post_scope.route('/post_user', methods=['GET', 'POST'])
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
        status = request.form['status']
        password = request.form['password']
        list_user = [avatar, dni, name, healthCoverage, email, phone, city, active, status, password]
        list_complet = post_userAdmin(list_user)
    return redirect(url_for("view.view_admin"))

@post_scope.route('/post_healthCoverage', methods=['GET', 'POST'])
def post_healthCoverage():
    if request.method == 'POST':
        logo = request.form['logo']
        name = request.form['name']
        plan = request.form['plan']
        list_healthCoverage = [logo, name, plan]
        list_complet = post_healthAdmin(list_healthCoverage)
    return redirect(url_for("view.view_admin"))

@post_scope.route('/post_clinic', methods=['GET', 'POST'])
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
    return redirect(url_for("view.view_admin"))

@post_scope.route('/contact', methods=['GET', 'POST'])
def post_contactIndex():
    if request.method == 'POST':
        name = request.form['name_message']
        email = request.form['email_message']
        message = request.form['text_message']
        contact_form = [name, email, message]
        contact = post_contact(contact_form)
    return redirect(url_for("view.view_home"))

@post_scope.route('/post_appointment', methods=['GET', 'POST'])
def post_appointment():
    if request.method == 'POST':
        user_id = request.form['user_id']
        appointmentDate = request.form['appointmentDate']
        observations = request.form['observations']
        speciality = request.form['speciality']
        modality = request.form['modality']
        appointment_form = [
            user_id, appointmentDate, observations, speciality, modality
        ]
        new_appointment = post_userAppointment(appointment_form)
        userSession = user_id
        load_user(userSession)
    return redirect(url_for("view.view_portal_appointments", _id=user_id))

# Ruta para registar usuario desde el login
@post_scope.route('/post_register', methods=['GET', 'POST'])
def post_register():
    if request.method == 'POST':
        avatar = request.form['avatar']
        dni = request.form['dni']
        name = request.form['name']
        password = request.form['password']
        # password_hash = generate_password_hash(password)  # Para hashear contraseñas al momento del registro
        healthCoverage = request.form['healthCoverage']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        status = request.form['status']
        active = request.form['active']
        user_register = [avatar, dni, name, healthCoverage, email, phone, city, active, status, password]
        user_register = post_userRegister(user_register)
    return redirect("/")

# Ruta para realizar el Login, parcial. Toca Agregar WTF 
@post_scope.route("/login", methods=['GET', 'POST'])
def post_login():
    if request.method == 'POST':
        dni = request.form['dni']
        # Elimino "posibles" espacios en blanco
        clean_inputDni = dni.strip()                        
        password = request.form['password']
        # Elimino "posibles" espacios en blanco
        clean_inputPassword = password.strip()              
        total_Users = get_login()
        for user in total_Users:
            dni_bd = user["dni"]
            # Elimino "posibles" espacios en blanco
            clean_dniBd = dni_bd.strip()                     
            password = user["password"]             # Para Hashear las contraseñas | password_hash = check_password_hash(password) 
            status_bd = user["status"]
            if clean_inputDni == clean_dniBd and clean_inputPassword == password and status_bd == "Administrador": 
                list_adminDoctors = view_doctors()
                list_adminUsers = view_users()
                list_healthCoverage = view_healthCoverage()
                list_adminClinics = view_clinics()
                data_admin = [list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics]
                user_login = [{  
                        "_id": user["_id"], 
                        "dni": user["dni"], 
                        "name": user["name"], 
                        "healthCoverage": user["healthCoverage"], 
                        "email": user["email"], 
                        "phone": user["phone"],
                        "city": user["city"],
                        "active": user["active"], 
                        "status": user["status"], 
                        "password": user["password"] 
                    }]
                userSession = user["dni"]
                load_user(userSession)
                return render_template("admin.html", data_admin=data_admin, appointmentButton=False, user_login=user_login, firstLogin=False)
            elif clean_inputDni == clean_dniBd and clean_inputPassword == password  and status_bd == "Usuario": 
                user_login = [{  
                    "_id": user["_id"], 
                    "dni": user["dni"], 
                    "name": user["name"], 
                    "healthCoverage": user["healthCoverage"], 
                    "email": user["email"], 
                    "phone": user["phone"],
                    "city": user["city"],
                    "active": user["active"], 
                    "status": user["status"], 
                    "password": user["password"] 
                }]
                userSession = user["dni"]
                load_user(userSession)
                return render_template("appointment.html", user_login=user_login)
        if clean_inputDni != clean_dniBd and clean_inputPassword != password:
            error_message = "Credenciales Inválidas"
            flash(error_message)
            list_doctors = view_doctorsHome()
            list_clinics = view_clinicsHome()
            return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics, title="admin", firstLogin=True)
                                

@login_manager.user_loader
def load_user(user_id):
    session['user_id'] = user_id
    # user_data = session[user_id]
    return user_id

@login_manager.unauthorized_handler
def unauthorized():
    list_doctors = view_doctorsHome()
    list_clinics = view_clinicsHome()
    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics, title="admin", firstLogin=True)

