from crypt import methods
from distutils.debug import DEBUG
from doctest import debug
import imp
from pickle import TRUE
from urllib import request
from flask import Flask, Response, request
import pymongo
import json

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

if __name__ == "__main__":
    app.run(port=8080, debug=TRUE)