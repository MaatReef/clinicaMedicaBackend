from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId

# Cada una de las clases en el modelo realiza la conexión correspondiente de acuerdo a lo que sea necesario.

class Appointments:
    def toList_appointments():
        db_appointments = db.appointments.find()
        return db_appointments

    # Old code
    # def delete_appointment(_id):
    #     # print(_id)
    #     query = {"_id": ObjectId(_id)}
    #     deleteOne_appointment = db.appointments.delete_one(query)
    #     return deleteOne_appointment

    # def edit_userAppointment(appointment):
    #     print(appointment)
    #     search = {"_id": ObjectId(appointment[1])}
    #     query = {
    #         '$set': {  
    #             "appointmentDate": appointment[2],
    #             "observations": appointment[3],
    #             "speciality": appointment[4],
    #             "modality": appointment[5]
    #         }
    #     }
    #     editOne_appointment = db.appointments.update_one(search, query)
    #     return editOne_appointment

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
