# Traigo el modelo que realiza la búsqueda en la bd
from app.models.Doctors import Doctors
from app.models.Clinics import Clinics
from app.models.Contacts import Contacts
from app.models.Doctors import Doctors
from app.models.HealthCoverage import HealthCoverage
from app.models.Specialities import Specialities
from app.models.Users import Users

def view_doctorsHome():
    dblist_doctors = Doctors.toList_doctorsAdmin()

    total_Doctors = []
    for doctor in dblist_doctors:
        total_Doctors.append(doctor)
        
    dblist_doctors.close()
    return total_Doctors

def view_clinicsHome():
    dblist_clinics = Clinics.toList_clinicsAdmin()

    total_clinics = []
    for clinic in dblist_clinics:
        total_clinics.append(clinic)
    
    dblist_clinics.close()
    return total_clinics

# Post : Funciones para Agregar filtrando la Data en la base de Datos
def post_contact(contact):
    user_contact = Contacts.post_contact(contact)
    return user_contact

# Get : User para corroborar en la base de Datos el acceso
def get_login():
    dblist_users = Users.toList_usersAdmin()
    total_Users = []
    for user in dblist_users:
        usuario_unique = {  
            "_id": user["_id"], 
            "dni": user["dni"], 
            "name": user["name"], 
            "healthCoverage": user["healthCoverage"], 
            "email": user["email"], 
            "phone": user["phone"],
            "city": user["address"]["city"],
            "active": user["active"], 
            "status": user["status"], 
            "password": user["password"] 
        }
        total_Users.append(usuario_unique)

    dblist_users.close()
    return total_Users