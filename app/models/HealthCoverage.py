from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId


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