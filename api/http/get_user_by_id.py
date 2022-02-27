from flask import Flask, Response, request, jsonify,  Blueprint
from api.service import list_users
import json
from bson.objectid import ObjectId

get_user_by_id = Blueprint('get_user_by_id', __name__)

@get_user_by_id.route("/getUser", methods=["GET"])
def list_user_by_id():
    id = request.form["id"]
    objInstance = ObjectId(id)
    try:
        data =  list_users.list_user_by_id(id)
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
            response= json.dumps({"message": "cannot find this user"}),
            status=404,
            mimetype="application/json"
        ) 
