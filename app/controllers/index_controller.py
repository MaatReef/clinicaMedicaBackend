# Traigo el modelo que realiza la búsqueda en la bd
from app.models.models import Doctors, Clinics, Contacts

def view_doctors():
    dblist_doctors = Doctors.toList_doctorsAdmin()

    total_Doctors = []
    for doctor in dblist_doctors:
        total_Doctors.append(doctor)
        
    dblist_doctors.close()
    return total_Doctors


def view_clinics():
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
