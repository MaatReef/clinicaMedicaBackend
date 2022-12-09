from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId

class Clinics:
    def toList_clinicsAdmin():
        db_clinicsAdmin = db.clinics.find()
        return db_clinicsAdmin

    def delete_clinicAdmin(_id):
        query = {"_id": ObjectId(_id)}
        deleteOne_clinicAdmin = db.clinics.delete_one(query)
        return deleteOne_clinicAdmin

    def edit_clinicAdmin(list_clinic):
        search = {"_id": ObjectId(list_clinic[0])}
        query = {
            '$set': {  
                "name": list_clinic[1], 
                "scheduleAttention": list_clinic[2], 
                "email": list_clinic[3], 
                "phone": list_clinic[4], 
                "address": { "city": list_clinic[5] },
            }
        }
        editOne_clinicAdmin = db.clinics.update_one(search, query)
        return editOne_clinicAdmin

    def post_clinicAdmin(list_clinic):
        query = {   
            "name": list_clinic[0], 
            "scheduleAttention": list_clinic[1], 
            "email": list_clinic[2], 
            "phone": list_clinic[3],
            "address": { "city": list_clinic[4] },
            "photo": list_clinic[5]
        } 
        postOne_clinicAdmin = db.clinics.insert_one(query)
        return postOne_clinicAdmin
