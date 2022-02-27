from flask import Flask, Response, request, jsonify,  Blueprint
from api.service import list_users as ls
import json
from bson.objectid import ObjectId

get_users = Blueprint('get_users', __name__)

@get_users.route("/getUsers", methods=["GET"])
def list_users():
    try:
        data =  ls.list_users()
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