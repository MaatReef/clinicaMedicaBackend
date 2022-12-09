# Traigo los modelos que realizan la búsqueda en la bd
from app.models.Doctors import Doctors
from app.models.Clinics import Clinics
from app.models.Contacts import Contacts
from app.models.Doctors import Doctors
from app.models.HealthCoverage import HealthCoverage
from app.models.Specialities import Specialities
from app.models.Users import Users 
from app.models.Appointments import Appointments

# View_: Funciones que se encargan de presentar la Data
def view_doctors():
    dblist_doctors = Doctors.toList_doctorsAdmin()

    total_Doctors = []
    for doctor in dblist_doctors:
        total_Doctors.append(doctor)
    
    dblist_doctors.close()
    return total_Doctors

def get_sessionUser(_id):
    sessionUser = Users.get_sessionUser(_id)
    # print(sessionUser)
    return sessionUser

def view_users():
    dblist_Users = Users.toList_usersAdmin()

    total_Users = []
    for user in dblist_Users:
        total_Users.append(user)

    dblist_Users.close()
    return total_Users

def view_healthCoverage():
    dblist_HealthCoverage = HealthCoverage.toList_healthCoverage()

    total_healthCoverage = []
    for healthCoverage in dblist_HealthCoverage:
        total_healthCoverage.append(healthCoverage)
    
    dblist_HealthCoverage.close()
    return total_healthCoverage

def view_clinics():
    dblist_clinics = Clinics.toList_clinicsAdmin()

    total_clinics = []
    for clinic in dblist_clinics:
        total_clinics.append(clinic)
    
    dblist_clinics.close()
    return total_clinics


def view_appointments(_id):
    sessionUser = Users.get_sessionUser(_id)
    dblist_appointments = Appointments.toList_appointments()

    total_appointments = []
    for appointment in dblist_appointments:
        total_appointments.append(appointment)
    dblist_appointments.close()
    return total_appointments


# Delete_ : Funciones para Eliminar la data filtrada en la base de Datos
def delete_doctorAdmin(_id):
    delete_doctor = Doctors.delete_doctorAdmin(_id)
    return 
    
def delete_clinicAdmin(_id):
    delete_clinic = Clinics.delete_clinicAdmin(_id)
    return 

def delete_coverageAdmin(_id):
    delete_coverage = HealthCoverage.delete_coverageAdmin(_id)
    return delete_coverage

def delete_userAdmin(_id):
    delete_user = Users.delete_userAdmin(_id)
    return delete_user

def delete_appointment(_id):
    delete_appointment = Appointments.delete_appointment(_id)
    return delete_appointment


# Edit_ : Funciones para Editar la Data filtrada en la base de Datos
def edit_coverageAdmin(list_coverage):
    # Si la opción es seleccionada le asigno el logo por defecto asociado a la obra social.    
    if list_coverage[4] == "OSECAC":
        list_coverage[4] = "assets/coverages/osecac.jpeg"
    elif list_coverage[4] == "IOMA":
        list_coverage[4] = "assets/coverages/ioma.png"
    elif list_coverage[4] == "OSDE":
        list_coverage[4] = "assets/coverages/osde.png"
    elif list_coverage[4] == "Swiss-medical":
        list_coverage[4] = "assets/coverages/swiss.png"
    
    list_complet = HealthCoverage.edit_coverageAdmin(list_coverage)
    return list_complet
    
def edit_userAdmin(list_user):
    list_complet = Users.edit_userAdmin(list_user)
    return list_complet

def edit_doctorAdmin(list_doctor):
    list_complet = Doctors.edit_doctorAdmin(list_doctor)
    return list_complet

def edit_clinicAdmin(list_clinic):
    list_complet = Clinics.edit_clinicAdmin(list_clinic)
    return list_complet

# def edit_userAppointment(appointment):
#     appointment = Appointments.edit_userAppointment(appointment)
#     return appointment


# Post : Funciones para Agregar filtrando la Data en la base de Datos
def post_doctorAdmin(list_doctor):          
    # Si la imagen no es seleccionada le agrego la imagen por defecto
    if list_doctor[3] == '':
        list_doctor[3] = "assets/default-user.png" 
    else:                                   
        # Si se selecciona alguna también, debido al servidor por el momento
        list_doctor[3] = "assets/default-user.png"
    list_complet = Doctors.post_doctorAdmin(list_doctor)
    return list_complet

def post_userAdmin(list_user):              
    # Si la imagen no es seleccionada le agrego la imagen por defecto
    if list_user[0] == '':
        list_user[0] = "assets/default-user.png" 
    else:                                   
        # Si se selecciona alguna también, debido al servidor por el momento
        list_user[0] = "assets/default-user.png"
    list_complet = Users.post_userAdmin(list_user)
    return list_complet

def post_healthAdmin(list_healthCoverage):  
    # Si la opción es seleccionada le asigno el logo por defecto asociado a la obra social
    if list_healthCoverage[0] == "OSECAC":
        list_healthCoverage[0] = "assets/coverages/osecac.jpeg"
    elif list_healthCoverage[0] == "IOMA":
        list_healthCoverage[0] = "assets/coverages/ioma.png"
    elif list_healthCoverage[0] == "OSDE":
        list_healthCoverage[0] = "assets/coverages/osde.png"
    elif list_healthCoverage[0] == "Swiss-medical":
        list_healthCoverage[0] = "assets/coverages/swiss.png"
    list_complet = HealthCoverage.post_healthAdmin(list_healthCoverage)
    return list_complet

def post_clinicAdmin(list_clinic):
    list_clinic = Clinics.post_clinicAdmin(list_clinic)
    return list_clinic

def post_userAppointment(appointment):
    appointment = Appointments.post_userAppointment(appointment)
    return appointment

def post_userRegister(user_register):              
    # Si la imagen no es seleccionada le agrego la imagen por defecto
    if user_register[0] == '':
        user_register[0] = "assets/default-user.png" 
    else:                                   
        # Si se selecciona alguna también, debido al servidor por el momento
        user_register[0] = "assets/default-user.png"
    user_register = Users.post_userRegister(user_register)
    return user_register