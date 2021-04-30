from app import app
from app.models.users import User

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return 'Login route'

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    return {}, 201