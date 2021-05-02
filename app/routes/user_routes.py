from app.models.users import User
from flask.globals import current_app as app
from flask import request
from flask_login import login_user

from app.database import mongo

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        if not request.json:
            return {}, 400
        if request.json.get('username') is None or request.json.get('password_hash') is None:
            return {}, 400
        if not User.login_user(username=request.json['username'], password_hash=request.json['password_hash']): # validate password
            return {}, 401
        user = User.get_by_username(request.json['username']) 
        login_user(user)
        return {}, 200

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'POST':
        if not request.json:
            return {}, 400
        if request.json.get('username') is None or request.json.get('password_hash') is None or request.json.get('email') is None:
            return {}, 400
        if not User.register_user(username=request.json['username'], password_hash=request.json['password_hash'], email=request.json['email']):
            return {}, 403
        return {}, 201