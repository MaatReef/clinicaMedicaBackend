from app.database.connection import db          
# Traemos la base de datos
from bson.objectid import ObjectId


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
