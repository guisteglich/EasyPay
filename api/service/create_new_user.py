from urllib import response
from api.extensions import mongo as db

def create_new_user(user):
    response = db.insert_user(user)
    return response