# Hacemos la instancia de nuestro Framework
from flask import Flask
from pymongo import 
from controlador import *       # Me traigo el controlador

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




