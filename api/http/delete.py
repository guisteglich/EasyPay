
from sqlalchemy import delete

from flask import Flask, Response, request, jsonify,  Blueprint
from api.service import delete_user
import json
from bson.objectid import ObjectId

delete = Blueprint('delete', __name__)

@delete.route("/delete/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = delete_user(id)
        return Response(
            response= json.dumps({"message": "user deleted"}),
            status=200,
            mimetype="application/json"
        )  
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({"message": "cannot delete this user"}),
            status=500,
            mimetype="application/json"
        ) 
