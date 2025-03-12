from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local

#Base de datos remota
db_client = MongoClient("mongodb+srv://christian:test@cluster0.s54ek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test