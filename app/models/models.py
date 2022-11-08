from app.database.connection import db          # Traemos la base de datos

class Doctors:
    db_doctors = db.doctors.find()              # Dentro de la base de datos, accedo a doctors.. Con la función find() de mongo db
    db_doctorsAdmin = db.doctors.find()        
    
class Clinics:
    db_clinics = db.clinics.find()
    db_clinicsAdmin = db.clinics.find()        

class HealthCoverage:
    db_healthCoverage = db.healthCoverage.find()

class Users:
    db_usersAdmin = db.users.find()

# class Specialities:
    # db_specialities = db.specialities.find()