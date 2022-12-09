from flask import Blueprint, url_for, render_template, redirect, request, session, flash
# from flask_login import logout_user
# from werkzeug.security import generate_password_hash, check_password_hash     
# Para "hashear" contraseñas y luego comparar el hash con el tecto plano

# Traigo la listas capturada desde el controlador.
from app.controllers.index_controller import *                                  
from app.controllers.admin_controller import *
from app.models.Users import Users
from flask_login import login_user, LoginManager, login_required, logout_user, current_user


# La carpeta views posee los ficheros estáticos
view_scope = Blueprint("view", __name__)   


# View: Las siguientes rutas se encargan de presentar la data traída desde la Base de DATOS
@view_scope.route("/", methods=['GET'])
def view_home():
    list_doctors = view_doctorsHome()
    list_clinics = view_clinicsHome()
    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics, title="admin", firstLogin=True)

@view_scope.route("/admin", methods=['GET'])
@login_required
def view_admin():
    list_adminDoctors = view_doctors()
    list_adminUsers = view_users()
    list_healthCoverage = view_healthCoverage()
    list_adminClinics = view_clinics()
    data_admin = [list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics]
    return render_template("admin.html", data_admin=data_admin, appointmentButton=True)

@view_scope.route("/appointment", methods=['GET', 'POST'])
@login_required
def view_appointment():
    return render_template("appointment.html")

# @view_scope.route("/portal", methods=['GET'])
# @login_required
# def view_portal():
#     return render_template("portal.html")

@view_scope.route("/portal/<_id>", methods=['GET'])
def view_portal_appointments(_id):
    if session.get('user_id'):
        userSession = Users.get_sessionUser(_id)
        return render_template("portal.html", user=userSession)
    else:
        list_doctors = view_doctorsHome()
        list_clinics = view_clinicsHome()
        return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics, title="admin", firstLogin=True)


@view_scope.route("/register", methods=['GET'])
def view_register():
    return render_template("register.html")


