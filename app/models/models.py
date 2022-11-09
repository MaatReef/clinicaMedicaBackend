from app.database.connection import db          # Traemos la base de datos

class Doctors:
    def toList_doctorsAdmin():
        db_doctorsAdmin = db.doctors.find()
        return db_doctorsAdmin   
    
class Clinics:
    def toList_clinicsAdmin():
        db_clinicsAdmin = db.clinics.find()
        return db_clinicsAdmin

class HealthCoverage:
    def toList_healthCoverage():
        db_healthCoverage = db.healthCoverage.find()
        return db_healthCoverage

class Users:
    def toList_usersAdmin():
        db_usersAdmin = db.users.find()
        return db_usersAdmin

class Specialities:
    def toList_specialitiesAdmin():
        db_specialitiesAdmin = db.specialities.find()
        return db_specialitiesAdmin