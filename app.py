from crypt import methods
from distutils.debug import DEBUG
from doctest import debug
import imp
from pickle import TRUE
from traceback import print_tb
from urllib import request
from flask import Flask, Response, request, jsonify
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

try: 
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017)
    print("CONNECTION TO DB SUCCESSFULLY")

    db = mongo.EasyPay
except:
    print("ERROR CONNECT TO DB")

@app.route("/")
def home():
    return "this is a home page"

@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            "name": request.form["name"], 
            "lastName": request.form["lastName"], 
            "email": request.form["email"]
            }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response= json.dumps({
                "message": "user created with successfully", 
                "id": f"{dbResponse.inserted_id}"
                }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return 400

@app.route("/getUsers", methods=["GET"])
def list_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response= json.dumps(data),
            status=200,
            mimetype="application/json"
        ) 
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({"message": "cannot read users"}),
            status=500,
            mimetype="application/json"
        ) 

@app.route("/getUser", methods=["GET"])
def list_user_by_id():
    id = request.form["id"]
    objInstance = ObjectId(id)
    try:
        data =  list(db.users.find({"_id": objInstance}))
        for user in data:
            user["_id"] = str(user["_id"])
        print(data) #descobrir como mandar essas informações via json.
        return Response(
            response= json.dumps(data),
            status=200,
            mimetype="application/json"
        ) 
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({"message": "cannot find that user"}),
            status=500,
            mimetype="application/json"
        ) 

if __name__ == "__main__":
    app.run(port=8080, debug=TRUE)