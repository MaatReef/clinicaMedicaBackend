from app.models.models import Doctors, Clinics      # Traigo el modelo que realiza la búsqueda en la bd


def view_doctors():
    dblist_doctors = Doctors.toList_doctorsAdmin()

    total_Doctors = []
    for doctor in dblist_doctors:
        total_Doctors.append(doctor)
        
    dblist_doctors.close()
    return total_Doctors


def view_clinics():
    dblist_clinics = Clinics.toList_clinicsAdmin()

    total_clinics = []
    for clinic in dblist_clinics:
        total_clinics.append(clinic)
    
    dblist_clinics.close()
    return total_clinics