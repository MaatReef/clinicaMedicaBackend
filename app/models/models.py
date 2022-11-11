from app.database.connection import db          # Traemos la base de datos

class Doctors:
    def toList_doctorsAdmin():
        db_doctorsAdmin = db.doctors.find()
        return db_doctorsAdmin   
    
    def delete_doctorAdmin(dni):
        query = {"dni": dni}
        delete_doctorsAdmin = db.doctors.delete_one(query)
        return delete_doctorsAdmin
    
class Clinics:
    def toList_clinicsAdmin():
        db_clinicsAdmin = db.clinics.find()
        return db_clinicsAdmin

    def delete_clinicAdmin(id):
        query = {"id": id}
        deleteOne_clinicAdmin = db.clinics.delete_one(query)
        return deleteOne_clinicAdmin

class HealthCoverage:
    def toList_healthCoverage():
        db_healthCoverage = db.healthCoverage.find()
        return db_healthCoverage
    
    def delete_coverageAdmin(id):
        query = {"id": id}
        deleteOne_coverageAdmin = db.healthCoverage.delete_one(query)
        return deleteOne_coverageAdmin

class Users:
    def toList_usersAdmin():
        db_usersAdmin = db.users.find()
        return db_usersAdmin

    def delete_userAdmin(dni):
        query = {"dni": dni}
        deleteOne_userAdmin = db.users.delete_one(query)
        return deleteOne_userAdmin

class Specialities:
    def toList_specialitiesAdmin():
        db_specialitiesAdmin = db.specialities.find()
        return db_specialitiesAdmin
