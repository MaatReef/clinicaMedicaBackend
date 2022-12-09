from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId

class Doctors:
    def toList_doctorsAdmin():
        db_doctorsAdmin = db.doctors.find()
        return db_doctorsAdmin   
    
    def delete_doctorAdmin(_id):
        query = {"_id": ObjectId(_id)}
        delete_doctorsAdmin = db.doctors.delete_one(query)
        return delete_doctorsAdmin

    def edit_doctorAdmin(list_doctor):
        search = {"_id": ObjectId(list_doctor[0])}
        query = {
            '$set': {
                "dni": list_doctor[1], 
                "name": list_doctor[2], 
                "speciality": list_doctor[3], 
                "email": list_doctor[4], 
                "address": { "city": list_doctor[5] }, 
                "scheduleAttention": list_doctor[6], 
                "active": list_doctor[7],
            }
        }
        editOne_doctorAdmin = db.doctors.update_one(search, query)
        return editOne_doctorAdmin

    def post_doctorAdmin(list_doctor):
        query = {   
            "dni": list_doctor[0], 
            "name": list_doctor[1], 
            "email": list_doctor[2], 
            "avatar": list_doctor[3], 
            "scheduleAttention": list_doctor[4], 
            "speciality": list_doctor[5],
            "active": list_doctor[6], 
            "attention": list_doctor[7] 
        }
        postOne_doctorAdmin = db.doctors.insert_one(query)
        return postOne_doctorAdmin
    