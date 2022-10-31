from app.models.models import Doctors               # Traigo el modelo que realiza la búsqueda en la bd

def index():

    list_doctors = []                               # Lo recorro con el for y le agrego los doctores
    for doctor in Doctors.doctors:
        # print(doctor["name"])                     # Lo vemos la lista de doctores desdel la consola.
        doctor_add = doctor["name"]
        list_doctors.append(doctor_add)             # Agregamos la data a la lista
    
    Doctors.doctors.close()                         # Cierro el cursor que se abre al buscar dentro de mongo
    
    return list_doctors

list_doctors = index()