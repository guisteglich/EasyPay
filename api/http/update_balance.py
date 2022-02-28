from crypt import methods
from flask import Flask, Response, request, jsonify,  Blueprint
from psutil import users 
from api.service import update_balance as service 
from api.service import list_users
import json
from bson.objectid import ObjectId


balance_update = Blueprint('balance_update', __name__)

@balance_update.route("/updateBalance/<id>", methods=["PATCH"])
def update_balance(id):
    value = request.form["value"]
  
    try:
        data =  list_users.list_user_by_id(id)
        user = data[0]
        balance = user["balance"]
        dbResponse = service.balance_update(id, value, balance)
        return Response(
            response= json.dumps({"message": "user balance updated"}),
            status=200,
            mimetype="application/json"
        ) 

    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({"message": "cannot update balance of this user"}),
            status=500,
            mimetype="application/json"
        ) 