# Hacemos la instancia de nuestro Framework
from flask import Flask, url_for, render_template
from pymongo import MongoClient

import os   # Os, operating system para manipular la variable de entorno
from dotenv import load_dotenv  # Ya instalado con con pip install python-dotenv


app = Flask(__name__) 

load_dotenv()  # Carga todo el contenido de .env en variables de entorno, de manera global
DB_TOKEN = os.environ.get("MONGO_URI")  # MONGO_URI tiene el string la conexión en .env para conectar con MONGODB
client = MongoClient(DB_TOKEN)          # Conectamos con la función MongoClient que provee pymongo

db = client.CUDI                        # Accedemos a la base de datos, la nombre CUDI
#print(db)                              # Para ver la base de datos desde consola.


# ServerStat = db.command("serverStatus")       # Para ver el estado del servidor y si todo está okey
# print(ServerStat)


# Decorador @, expande las funciones de una función
@app.route("/", methods=['GET'])
def index():

    doctors = db.doctors.find()                     # Dentro de la base de datos, accedo a doctors.. Con la función find() de mongo db

    list_doctors = []                               # Lo recorro con el for y le agrego los usuarios
    for doctor in doctors:
        print(doctor["name"])                       # Lo vemos desde la consola.
        doctor_add = doctor["name"]
        list_doctors.append(doctor_add)
    
    doctors.close()                                 # Cierro el cursor que se abre al buscar dentro de mongo

    return render_template("index.html", list_doctors=list_doctors)  # Renderizo la plantilla y le paso como argumento la lista 

