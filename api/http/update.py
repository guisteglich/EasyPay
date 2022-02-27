from flask import Flask, Response, request, jsonify,  Blueprint
from api.service import update_user as service
import json
from bson.objectid import ObjectId


update_user = Blueprint('update_user', __name__)

@update_user.route("/update/<id>", methods=["PATCH"])
def update(id):
    local = request.form["local"]
    value = request.form["value"]
    newvalues = { "$set": { local: value } }
    try:
        dbResponse = service.update(id, newvalues)
        return Response(
            response= json.dumps({"message": "user updated"}),
            status=200,
            mimetype="application/json"
        ) 

    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({"message": "cannot update this user"}),
            status=500,
            mimetype="application/json"
        ) 