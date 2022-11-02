from app.database.connection import db      # Traemos la base de datos

class Doctors:
    db_doctors = db.doctors.find()        # Dentro de la base de datos, accedo a doctors.. Con la función find() de mongo db
    
class Clinics:
    db_clinics = db.clinics.find()

# class HealthCoverage:

# class Specialities:

# class Users: