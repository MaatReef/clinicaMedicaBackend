from flask import Blueprint, url_for, render_template, redirect, request, session, flash
from flask_login import logout_user
# from werkzeug.security import generate_password_hash, check_password_hash     
# Para "hashear" contraseñas y luego comparar el hash con el tecto plano

# Traigo la listas capturada desde el controlador.
from app.controllers.index_controller import *                                  
from app.controllers.admin_controller import *
from app.models.Users import Users

# La carpeta views posee los ficheros estáticos
global_scope = Blueprint("views", __name__)   

@global_scope.route('/cudi')
def externals():
    return redirect("https://www.cudi.ar")

@global_scope.route("/logout")
def logout():
    if session.get('user_id'):
        del session['user_id']
        logout_user()
        # prevent flashing automatically logged out message
    
    print("*")
    print("*")
    print("*")
    print("*")
    print("*")
    print("*")
    print("*")
    print("*")
    # user_id = session[user_id] 
    # # salir = session[user_id]
    # ahora = session['user_id']
    # print("Ahoooora")
    # print(ahora)
    # print("session['user_id']")
    # session.clear()
    # print(ahora)

    # session['user_id'] = ""
    # print(session[user_id] )
    # session[user_id] 
    # logout_user()
    
    list_doctors = view_doctorsHome()
    list_clinics = view_clinicsHome()
    return render_template("index.html", list_doctors=list_doctors, list_clinics=list_clinics, title="admin", firstLogin=True)


@global_scope.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)

