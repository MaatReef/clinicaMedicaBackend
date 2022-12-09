from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

class Users():
    def toList_usersAdmin():
        db_usersAdmin = db.users.find()
        return db_usersAdmin

    def get_sessionUser(_id):
        query = {"_id": ObjectId(_id)}
        sessionUser = db.users.find_one(query)
        return sessionUser

    def delete_userApp(appointment_form):
        deleteOne_userAppointment = db.users.update_one(
            {"_id": ObjectId(appointment_form[0])},
            {'$pull': {'appointments': {"_id": ObjectId(appointment_form[1])}}}
        )   
        return deleteOne_userAppointment

    def edit_userApp(appointment_form):
        editOne_userAppointment = db.users.update_one(
            {
                '_id': ObjectId(appointment_form[0]),
                "appointments._id": ObjectId(appointment_form[1])
            },
            {'$set': {
                'appointments.$.appointmentDate': appointment_form[2],
                'appointments.$.observations': appointment_form[3],
                'appointments.$.speciality': appointment_form[4],
                'appointments.$.modality': appointment_form[5]
            }}
        )
        return editOne_userAppointment

    def delete_userAdmin(_id):
        query = {"_id": ObjectId(_id)}
        deleteOne_userAdmin = db.users.delete_one(query)
        return deleteOne_userAdmin

    def edit_userAdmin(list_user):
        search = {"_id": ObjectId(list_user[0])}
        query = {
            '$set': {  
                "avatar": list_user[1],     
                "dni": list_user[2], 
                "name": list_user[3], 
                "healthCoverage": list_user[4], 
                "email": list_user[5], 
                "phone": list_user[6], 
                "address": { "city": list_user[7] }, 
                "active": list_user[8],
                "status": list_user[9],
                "password": list_user[10]
            }
        }
        editOne_userAdmin = db.users.update_one(search, query)
        return editOne_userAdmin

    def post_userAdmin(list_user):
        query = {   
            "avatar": list_user[0], 
            "dni": list_user[1], 
            "name": list_user[2], 
            "healthCoverage": list_user[3], 
            "email": list_user[4], 
            "phone": list_user[5],
            "address": { "city": list_user[6] },
            "active": list_user[7],
            "status": list_user[8],
            "password": list_user[9]
        }
        postOne_userAdmin = db.users.insert_one(query)
        return postOne_userAdmin
    
    def post_userRegister(user_register):
        query = {   
            "avatar": user_register[0], 
            "dni": user_register[1], 
            "name": user_register[2], 
            "healthCoverage": user_register[3], 
            "email": user_register[4], 
            "phone": user_register[5],
            "address": { "city": user_register[6] },
            "active": user_register[7], 
            "status": user_register[8], 
            "password": user_register[9], 
        }
        postOne_userRegister = db.users.insert_one(query)
        return postOne_userRegister
