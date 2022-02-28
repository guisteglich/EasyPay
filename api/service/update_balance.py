from hashlib import new

from sqlalchemy import false
from api.extensions.mongo import update_user

def balance_update(id, value, balance):
    balance_value_updated = int(value) + int(balance)
    new_values = { "$set": { "balance": balance_value_updated } }
    response = update_user(id, new_values)
    return response

def balance_update_payer(id, value, balance):
    balance_value_updated = int(balance) - int(value)
    print("valor atualizado do pagador: ", balance_value_updated)
    if balance_value_updated < 0:
        print("if")
        return "not ok"
    else:
        print("entrei")
        new_values = { "$set": { "balance": balance_value_updated } }
        response = update_user(id, new_values)
        return response
        
