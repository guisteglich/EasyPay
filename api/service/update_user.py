from urllib import response
from api.extensions.mongo import update_user

def update(id, newvalues):
    response = update_user(id, newvalues)
    return response