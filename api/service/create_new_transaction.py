from sqlalchemy import false, true
from api.extensions import mongo as db
from api.service import list_users 
from api.service import update_balance  as service
from flask import Response
import json

def create_new_transaction(transaction):
    response = db.create_transaction(transaction)
    return response

def update_values_of_transaction(transaction):
    try:
        data_payer =  list_users.list_user_by_id(transaction["payer"])
        print("dados do pagador: ", data_payer)
        user_payer = data_payer[0]
        type_of_payer = user_payer["is_common_user"]
        balance_payer = user_payer["balance"]
        if type_of_payer != false:
            dbResponsePayer = service.balance_update_payer(
                transaction["payer"], 
                transaction["value"], 
                balance_payer)
            print("essa é a resposta do pagador: ", dbResponsePayer)
            if dbResponsePayer != "not ok":
                data_payee =  list_users.list_user_by_id(transaction["payee"])
                user_payee = data_payee[0]
                balance_payee = user_payee["balance"]
                dbResponsePayer = service.balance_update(
                    transaction["payee"], 
                    transaction["value"], 
                    balance_payee)
                return true
        else:
            return "not ok"
    except:
        return  "not ok"