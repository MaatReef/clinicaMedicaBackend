# Acá va lo del admin..
from app.models.models import Doctors, Clinics, Users, HealthCoverage    # Traigo los modelos que realizan la búsqueda en la bd

def view_doctors():
    
    list_adminDoctors = []                                 # Data para la tabla de Doctores de la sección Admin
    for doctor in Doctors.db_doctorsAdmin:
        only_doctor = []                    
        doctor_addId = doctor["dni"]
        only_doctor.append(doctor_addId)  

        doctor_addAvatar = doctor["avatar"]
        only_doctor.append(doctor_addAvatar)

        doctor_addName = doctor["name"]
        only_doctor.append(doctor_addName)

        doctor_addSpeciality = doctor["speciality"]
        only_doctor.append(doctor_addSpeciality)

        doctor_addEmail = doctor["email"]
        only_doctor.append(doctor_addEmail)

        doctor_addAttention = doctor["attention"]
        only_doctor.append(doctor_addAttention)

        doctor_addScheduleAtention = doctor["scheduleAttention"]
        only_doctor.append(doctor_addScheduleAtention)

        doctor_addActive = doctor["active"]
        only_doctor.append(doctor_addActive)  

        list_adminDoctors.append(only_doctor)             
    
    Doctors.db_doctors.close()                      
    return list_adminDoctors
list_adminDoctors = view_doctors()

def view_users():
    list_adminUsers = []                                    # Data para la tabla de Pacientes/Usuarios de la sección Admin
    for user in Users.db_usersAdmin:
        only_user = []                    
        user_addId = user["id"]
        only_user.append(user_addId)  

        user_addAvatar = user["avatar"]
        only_user.append(user_addAvatar)

        user_addName = user["name"]
        only_user.append(user_addName)

        user_addHealthCoverage = user["healthCoverage"]
        only_user.append(user_addHealthCoverage)

        user_addEmail = user["email"]
        only_user.append(user_addEmail)

        user_addPhone = user["phone"]
        only_user.append(user_addPhone)

        user_addCity = user["address"]["city"]
        only_user.append(user_addCity)

        user_addActive = user["active"]
        only_user.append(user_addActive)  

        list_adminUsers.append(only_user)             
    
    Users.db_usersAdmin.close()                      
    return list_adminUsers
list_adminUsers = view_users()

def view_healthCoverage():
    list_healthCoverage = []                                # Data para la tabla de las Obras Sociales de la sección Admin
    for healthCoverage in HealthCoverage.db_healthCoverage:
        only_healthCoverage = []
        healthCoverage_addId = healthCoverage["id"]
        only_healthCoverage.append(healthCoverage_addId)  

        healthCoverage_addLogo = healthCoverage["logo"]
        only_healthCoverage.append(healthCoverage_addLogo)

        healthCoverage_addName = healthCoverage["name"]
        only_healthCoverage.append(healthCoverage_addName)

        healthCoverage_addPlan = healthCoverage["plan"]
        only_healthCoverage.append(healthCoverage_addPlan)

        list_healthCoverage.append(only_healthCoverage)             
    
    HealthCoverage.db_healthCoverage.close()                      
    return list_healthCoverage
list_healthCoverage = view_healthCoverage()

def view_clinics():
    list_adminClinics = []                               # Data para la tabla de las Clínicas de la sección Admin
    for clinic in Clinics.db_clinicsAdmin:
        only_clinic = []                            
        id_clinicAdd = clinic["id"] 
        only_clinic.append(id_clinicAdd)   

        name_clinicAdd = clinic["name"] 
        only_clinic.append(name_clinicAdd)             

        scheduleAttention_clinicAdd = clinic["scheduleAttention"]
        only_clinic.append(scheduleAttention_clinicAdd)             
        
        email_clinicAdd = clinic["email"]
        only_clinic.append(email_clinicAdd)  

        phone_clinicAdd = clinic["phone"]
        only_clinic.append(phone_clinicAdd)             
        
        adress_clinicAdd = clinic["address"]["city"]
        only_clinic.append(adress_clinicAdd)  

        list_adminClinics.append(only_clinic)             

    Clinics.db_clinicsAdmin.close()                       
    return list_adminClinics
list_adminClinics = view_clinics()

