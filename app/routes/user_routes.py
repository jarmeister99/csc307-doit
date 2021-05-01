from flask.globals import current_app as app
from app.models.users import User

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return 'Login route'

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'POST':
        if not request.json:
            return {}, 400
        if not set(request.json.keys()).issubset({'username', 'password_hash', 'email'}):
            return {}, 400
        return {}, 201
    return {}, 202