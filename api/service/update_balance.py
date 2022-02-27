from hashlib import new
from api.extensions.mongo import update_user

def balance_update(id, new_values):
    response = update_user(id, new_values)
    return response
