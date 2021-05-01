from app.models.users import add_user, validate_password
from flask.globals import current_app as app
from flask import request

from app.database import mongo

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        if not request.json:
            return {}, 400
        if not set(request.json.keys()).issubset({'username', 'password_hash'}):
            return {}, 400
        if not validate_password(request.json['username'], request.json['password_hash']):
            return {}, 401
        return {}, 200
    return {}, 202

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'POST':
        if not request.json:
            return {}, 400
        if not set(request.json.keys()).issubset({'username', 'password_hash', 'email'}):
            return {}, 400
        if not add_user(request.json['username'], request.json['password_hash'], request.json['email']):
            return {}, 403
        return {}, 201
    return {}, 202