from flask import Blueprint, url_for, render_template, redirect, request, session, flash
# from flask_login import logout_user
# from werkzeug.security import generate_password_hash, check_password_hash     
# Para "hashear" contraseñas y luego comparar el hash con el tecto plano

# Traigo la listas capturada desde el controlador.
from app.controllers.index_controller import *                                  
from app.controllers.admin_controller import *
from app.models.Users import Users

# La carpeta views posee los ficheros estáticos
delete_scope = Blueprint("delete", __name__)   

# Delete: Las siguientes rutas se encargan de eliminar la data en la base de datos desde el formulario de la sección admin
@delete_scope.route('/delete_doctor/<_id>')
def delete_doctor(_id):
    delete = delete_doctorAdmin(_id)
    return redirect(url_for("view.view_admin"))
    
@delete_scope.route('/delete_clinic/<_id>' )
def delete_clinic(_id):
    delete = delete_clinicAdmin(_id)
    return redirect(url_for("view.view_admin"))
    
@delete_scope.route('/delete_coverage/<_id>')
def delete_coverage(_id):
    delete = delete_coverageAdmin(_id)
    return redirect(url_for("view.view_admin"))

@delete_scope.route('/delete_user/<_id>')
def delete_user(_id):
    delete = delete_userAdmin(_id)
    return redirect(url_for("view.view_admin"))

@delete_scope.route('/delete_appointment', methods=['GET', 'POST'])
def delete_userAppointment():
    if request.method == 'POST':
        user_id = request.form['user_id']
        _id = request.form['_id']
        appointment_form = [
            user_id, 
            _id,
        ]
        to_delete_appointment = Users.delete_userApp(appointment_form)
    return redirect(url_for("view.view_portal_appointments", _id=user_id))     
