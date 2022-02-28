from urllib import response
from api.extensions.mongo import delete_user, delete_transaction
 
def delete_user(id):
    response = delete_user(id)
    return response

def delete_transaction(id):
    response = delete_transaction(id)
    return response