import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.users import User
from flask_login import current_user

def test_login_no_data(client):
    resp = client.post('/login', json={})
    assert(resp.status_code == 400) # bad request

def test_login_incorrect_data(client):
    data = {'dont_care': 7, 'not_the_right_data': 10}
    resp = client.post('/login', json=data, content_type='application/json')
    assert(resp.status_code == 400) # bad request

def test_login_missing_password(client):
    data={'username': 'jared'}
    resp = client.post('/login', json=data, content_type='application/json') # log in user
    assert(resp.status_code == 400) # bad request

def test_login_correct_password(client, db):
    data = {'username': 'jared', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    resp = client.post('/register', json=data, content_type='application/json') # create user
    assert(not current_user.is_authenticated)

    data={'username': 'jared', 'password_hash': 0xABCD}
    resp = client.post('/login', json=data, content_type='application/json') # log in user
    assert(current_user.is_authenticated)

    assert(resp.status_code == 200)
    assert(current_user.username == 'jared') # ensure correct user was logged in

def test_login_incorrect_password(client, db):
    data = {'username': 'jared', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    resp = client.post('/register', json=data, content_type='application/json')
    assert(not current_user.is_authenticated)

    data={'username': 'jared', 'password_hash': 0xFFFF}
    resp = client.post('/login', json=data, content_type='application/json')

    assert(resp.status_code == 401)
    assert(not current_user.is_authenticated)

def test_login_nonexistent_user(client, db):
    data={'username': 'jared', 'password_hash': 0xFFFF}
    resp = client.post('/login', json=data, content_type='application/json')
    assert(resp.status_code == 401)
    assert(not current_user.is_authenticated)
