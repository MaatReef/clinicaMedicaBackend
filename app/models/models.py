from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId

# Cada una de las clases en el modelo realiza la conexión correspondiente de acuerdo a lo que sea necesario.
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
    

class Contacts:
    def toList_contact():
        db_contactAdmin = db.contact.find()
        return db_contactAdmin

    def post_contact(list_contact):
        query = {
            "name": list_contact[0],
            "email": list_contact[1],
            "message": list_contact[2]
        }
        postOne_contact = db.contacts.insert_one(query)
        return postOne_contact

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


class HealthCoverage:
    def toList_healthCoverage():
        db_healthCoverage = db.healthCoverage.find()
        return db_healthCoverage
    
    def delete_coverageAdmin(_id):
        query = {"_id": ObjectId(_id)}
        deleteOne_coverageAdmin = db.healthCoverage.delete_one(query)
        return deleteOne_coverageAdmin

    def edit_coverageAdmin(list_coverage):
        search = {"_id": ObjectId(list_coverage[0])}
        query = {
            '$set': {  
                "id": list_coverage[1], 
                "name": list_coverage[2], 
                "plan": list_coverage[3], 
                "logo": list_coverage[4]
            }
        }
        editOne_coverageAdmin = db.healthCoverage.update_one(search, query)
        return editOne_coverageAdmin
    
    def post_healthAdmin(list_healthCoverage):
        query = {   
            "logo": list_healthCoverage[0], 
            "name": list_healthCoverage[1], 
            "plan": list_healthCoverage[2] 
        }
        postOne_coverageAdmin = db.healthCoverage.insert_one(query)
        return postOne_coverageAdmin


class Users:
    def toList_usersAdmin():
        db_usersAdmin = db.users.find()
        return db_usersAdmin

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


class Specialities:
    def toList_specialitiesAdmin():
        db_specialitiesAdmin = db.specialities.find()
        return db_specialitiesAdmin

class Appointments:
    def toList_appointments():
        db_appointments = db.appointments.find()
        print(db_appointments)
        return db_appointments

    def delete_appointment(_id):
        print(_id)
        query = {"_id": ObjectId(_id)}
        deleteOne_appointment = db.appointments.delete_one(query)
        return deleteOne_appointment

    def edit_userAppointment(appointment):
        print(appointment)
        search = {"_id": ObjectId(appointment[1])}
        query = {
            '$set': {  
                "appointmentDate": appointment[2],
                "observations": appointment[3],
                "speciality": appointment[4],
                "modality": appointment[5]
            }
        }
        editOne_appointment = db.appointments.update_one(search, query)
        return editOne_appointment

    def post_userAppointment(appointment):
        query = {   
            "user_id": appointment[0],
            "appointmentDate": appointment[1], 
            "observations": appointment[2], 
            "speciality": appointment[3], 
            "modality": appointment[4]
        } 
        post_appointment = db.appointments.insert_one(query)
        post_appointment_into_session_user = db.users.update_one(
            {"_id": ObjectId(appointment[0])},
            {
                '$push': {
                    'appointments': query
                }
            }
        )
        return post_appointment_into_session_user
