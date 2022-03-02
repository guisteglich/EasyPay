from flask import Flask, Response, request, jsonify,  Blueprint
import json
from api.service import create_new_user as service
from api.extensions import send_confirmation as mail

create = Blueprint('create', __name__)

@create.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            "name": request.form["name"], 
            "lastName": request.form["lastName"], 
            "CPF": request.form["CPF"],
            "email": request.form["email"], 
            "balance": 0, 
            "is_common_user": request.form["is_common_user"]
            }       
        dbResponse = service.create_new_user(user)
        print(dbResponse.inserted_id)
        confirmation = mail.send_confirmation(user["name"], user["email"])
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
        return 404
