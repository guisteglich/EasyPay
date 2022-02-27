from flask import Flask, Response, request, jsonify

# app = Flask(__name__)

from api.http.create import create
from api.http.delete import delete
from api.http.get_user_by_id import get_user_by_id
from api.http.get_users import get_users
from api.http.update import update_user
from api.http.update_balance import balance_update

app = Flask(__name__)

app.register_blueprint(create)
app.register_blueprint(delete)
app.register_blueprint(get_user_by_id)
app.register_blueprint(get_users)
app.register_blueprint(update_user)
app.register_blueprint(balance_update)


@app.route("/")
def home():
    return "this is a home page"

if __name__ == "__main__":
    app.run(port=8080)