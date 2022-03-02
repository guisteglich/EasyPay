from urllib import response
import requests

def confirmation():
    r = requests.get('https://run.mocky.io/v3/8fafdd68-a090-496f-8c9a-3442cf30dae6')
    response = r.json()
    # print(response)

    return response["message"]



