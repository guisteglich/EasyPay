from dataclasses import dataclass
import pymongo
from bson.objectid import ObjectId

# from api.http.transaction import transaction


try: 
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017)
    print("CONNECTION TO DB SUCCESSFULLY")
    db = mongo.EasyPay
    # db.users.createIndex( { "email": 1 }, { unique: true } )
except:
    print("ERROR CONNECT TO DB")


def insert_user(user):
    dbResponse = db.users.insert_one(user)
    return dbResponse

def delete_user(id):
    dbResponse = db.users.delete_one({"_id": ObjectId(id)})
    return dbResponse

def find_users():
    data = list(db.users.find())
    for user in data:
        user["_id"] = str(user["_id"])
    return data

def find_user_by_id(id):
    data =  list(db.users.find({"_id": ObjectId(id)}))
    for user in data:
        user["_id"] = str(user["_id"])
    return data

def update_user(id, newvalues):
    dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},newvalues)
    return dbResponse

def create_transaction(transaction):
    dbResponse = db.transactions.insert_one(transaction)
    return dbResponse 

def delete_transaction(id):
    dbResponse = db.transactions.delete_one({"_id": ObjectId(id)})
    return dbResponse
