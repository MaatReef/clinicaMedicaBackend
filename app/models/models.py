from app.database.connection import db      # Traemos la base de datos

class Doctors:
    doctors = db.doctors.find()             # Dentro de la base de datos, accedo a doctors.. Con la función find() de mongo db
    
                                            # Igual sería para lo demás 
# class Clinics:

# class HealthCoverage:

# class Specialities:

# class Users: