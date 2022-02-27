from crypt import methods
from flask import Flask, Response, request, jsonify,  Blueprint 
from api.service import update_balance as service 
import json
from bson.objectid import ObjectId


balance_update = Blueprint('balance_update', __name__)

@balance_update.route("/updateBalance/<id>", methods=["PATCH"])
def update_balance(id):
    value = request.form["value"]
    newvalues = { "$set": { "balance": value } }
    try:
        dbResponse = service.balance_update(id, newvalues)
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