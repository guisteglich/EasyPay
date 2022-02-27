from urllib import response
from api.extensions.mongo import find_users, find_user_by_id

def list_users():
    response = find_users()
    return response

def list_user_by_id(id):
    response = find_user_by_id(id)
    return response