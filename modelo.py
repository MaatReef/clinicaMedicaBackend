from app import db                          # Me traigo la base de datos

class Doctors:
    doctors = db.doctors.find()             # Dentro de la base de datos, accedo a doctors.. Con la función find() de mongo db

# Lo mismo para la demás data
# class Clinics(db.model):

# class HealthCoverage(db.model):

# class Specialities(db.model):

# class Users(db.model):
