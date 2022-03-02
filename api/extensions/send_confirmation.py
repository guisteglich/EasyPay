# Install Courier SDK: pip install trycourier
from trycourier import Courier

def send_confirmation(name, email):

  client = Courier(auth_token="pk_prod_XQZGKEJ9P24C79QZF6H2XM5ATCEC")

  resp = client.send_message(
    message={
      "to": {
        "email": email
      },
      "content": {
        "title": "Welcome to EasyPay!",
        "body": "{{name}}, you have registered with our bank and are receiving a confirmation email."
      },
      "data":{
        "name": name
      }
    }
  )