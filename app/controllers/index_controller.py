from app.models.models import Doctors, Clinics      # Traigo el modelo que realiza la búsqueda en la bd

print(Doctors)

def view_doctors():
    list_doctors = []                               # Lo recorro con el for y le agrego los doctores
    for doctor in Doctors.doctors:
        print(doctor["name"])                       # Lo vemos la lista de doctores desdel la consola.
        doctor_add = doctor["name"]
        list_doctors.append(doctor_add)             # Agregamos la data a la lista
    
    Doctors.doctors.close()                         # Cierro el cursor que se abre al buscar dentro de mongo
    return list_doctors
    
list_doctors = view_doctors()


def view_clinics():
    list_clinics = []                               # Un Array total con otro array dentro
    for clinic in Clinics.clinics:
        only_clinic = []                            # Cada clinica es añadida dentro del array general.
        name_clinicAdd = clinic["name"]
        only_clinic.append(name_clinicAdd)             

        scheduleAttention_clinicAdd = clinic["scheduleAttention"]
        only_clinic.append(scheduleAttention_clinicAdd)             
        
        phone_clinicAdd = clinic["phone"]
        only_clinic.append(phone_clinicAdd)             
        
        adress_clinicAdd = clinic["address"]["city"]
        only_clinic.append(adress_clinicAdd)  

        photo_clinicAdd = clinic["photo"]
        only_clinic.append(photo_clinicAdd)  

        list_clinics.append(only_clinic)             # Agregamos una lista a la lista general

    Clinics.clinics.close()                         # Cierro el cursor que se abre al buscar dentro de mongo

    return list_clinics

list_clinics = view_clinics()