from pymongo import MongoClient
from config import Config                   # Traemos el objeto de configuración general

CONNECTION_BD = Config.MONGO_URI

client = MongoClient(CONNECTION_BD)         # Conectamos con la función MongoClient que provee pymongo

db = client.CUDI                            # Accedemos a la base de datos, nombrada como CUDI
# print(db)                               