from app import app                                 
from modelo import *                           # Traigo todo del modelo
from flask import url_for, render_template

# Decorador @, expande las funciones de una funció
@app.route("/", methods=['GET'])
def index():

    list_doctors = []                               # Lo recorro con el for y le agrego los doctores
    for doctor in Doctors.doctors:
        print(doctor["name"])                       # Lo vemos desde la consola.
        doctor_add = doctor["name"]
        list_doctors.append(doctor_add)
    
    Doctors.doctors.close()                                 # Cierro el cursor que se abre al buscar dentro de mongo

    return render_template("index.html", list_doctors=list_doctors)  # Renderizo la plantilla y le paso como argumento la lista 

