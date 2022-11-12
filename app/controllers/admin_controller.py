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

def delete_doctorAdmin(dni):
    delete_doctor = Doctors.delete_doctorAdmin(dni)
    
def delete_clinicAdmin(id):
    delete_clinic = Clinics.delete_clinicAdmin(id)

def delete_coverageAdmin(id):
    delete_coverage = HealthCoverage.delete_coverageAdmin(id)

def delete_userAdmin(dni):
    delete_user = Users.delete_userAdmin(dni)

# Edit
def edit_coverageAdmin(list_coverage):
    if list_coverage[4] == "OSECAC":
        list_coverage[4] = "assets/coverages/osecac.jpeg"
    elif list_coverage[4] == "IOMA":
        list_coverage[4] = "assets/coverages/ioma.png"
    elif list_coverage[4] == "OSDE":
        list_coverage[4] = "assets/coverages/osde.png"
    elif list_coverage[4] == "Swiss-medical":
        list_coverage[4] = "assets/coverages/swiss.png"
    
    list_complet = HealthCoverage.edit_coverageAdmin(list_coverage)
    
def edit_userAdmin(list_user):
    list_complet = Users.edit_userAdmin(list_user)

def edit_doctorAdmin(list_doctor):
    list_complet = Doctors.edit_doctorAdmin(list_doctor)

def edit_clinicAdmin(list_clinic):
    list_complet = Clinics.edit_clinicAdmin(list_clinic)