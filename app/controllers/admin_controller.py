# Acá va lo del admin..
from app.models.models import Doctors, Clinics, Users, HealthCoverage    # Traigo los modelos que realizan la búsqueda en la bd

def view_doctors():
    dblist_doctors = Doctors.toList_doctorsAdmin()

    total_Doctors = []
    for doctor in dblist_doctors:
        total_Doctors.append(doctor)
    
    dblist_doctors.close()
    return total_Doctors

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