from flask import Flask, Response, request,  Blueprint
import json

from sqlalchemy import false, true
from api.service import create_new_transaction as service
# from api.service import create_new_transaction
from api.extensions.mongo import delete_transaction

user_transaction = Blueprint('user_transaction', __name__)

@user_transaction.route("/transaction", methods=["POST"])
def transaction():
    try:
        transaction = {
            "value": request.form["value"], 
            "payer": request.form["payer"], 
            "payee": request.form["payee"]
            }       
        dbResponse = service.create_new_transaction(transaction)
        print(dbResponse.inserted_id)
        transaction_process = service.update_values_of_transaction(transaction)
        print("resposta processo de transição: ", transaction_process)
        if transaction_process !=  "not ok":
            return Response(
                response= json.dumps({
                    "message": "transaction done with success", 
                    "id": f"{dbResponse.inserted_id}"
                    }),
                status=200,
                mimetype="application/json"
            )        
        else:
            dbResponse = delete_transaction(id)
            pass
            # Response(
            #     response= json.dumps({"message": "error making transaction"}),
            #     status=500,
            #     mimetype="application/json"
            # )    
    except Exception as ex:
        print("excessão: ", ex)
        return Response(
            response= json.dumps({"message": "error making transaction"}),
            status=500,
            mimetype="application/json"
        ) 