from flask import Flask, Response, request, jsonify,  Blueprint
import json
from api.service import create_new_user as service

create = Blueprint('create', __name__)

@create.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            "name": request.form["name"], 
            "lastName": request.form["lastName"], 
            "email": request.form["email"], 
            "balance": 0
            }       
        dbResponse = service.create_new_user(user)
        print(dbResponse.inserted_id)
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
