from urllib import response
from api.extensions.mongo import delete_user
 
def delete_user(id):
    response = delete_user(id)
    return response