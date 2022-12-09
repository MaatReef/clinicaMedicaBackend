import os
from dotenv import load_dotenv              # Instalar con pip install python-dotenv

load_dotenv()                               # Carga todo el contenido de .env en variables de entorno


class Config:
    DEBUG = True

    MONGO_URI = os.environ.get("MONGO_URI") # Capto el string de la Base de datos

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"

    SECRET_KEY = "Q1@*2R2mFxka7bGat"

    
