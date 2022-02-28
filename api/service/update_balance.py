from hashlib import new
from api.extensions.mongo import update_user

def balance_update(id, value, balance):
    balance_value_updated = int(value) + int(balance)
    new_values = { "$set": { "balance": balance_value_updated } }
    response = update_user(id, new_values)
    return response
