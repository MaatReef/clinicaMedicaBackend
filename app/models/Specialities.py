from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId

class Specialities:
    def toList_specialitiesAdmin():
        db_specialitiesAdmin = db.specialities.find()
        return db_specialitiesAdmin