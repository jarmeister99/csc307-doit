"""
These testcases cover the /login route which is responsible for authenticating users.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask_login import current_user

def test_login_no_data(client):
    """
    This testcase tests the /login route with an empty payload
    """
    resp = client.post('/login', json={})
    assert resp.status_code == 400 # bad request

def test_login_incorrect_data(client):
    """
    This testcase tests the /login route with an incorrect payload
    """
    data = {'dont_care': 7, 'not_the_right_data': 10}
    resp = client.post('/login', json=data, content_type='application/json')
    assert resp.status_code == 400 # bad request

def test_login_missing_password(client):
    """
    This testcase tests the /login route with a missing password
    """
    data={'username': 'jared'}
    resp = client.post('/login', json=data, content_type='application/json') # log in user
    assert resp.status_code == 400 # bad request

def test_login_correct_password(client, db):
    """
    This testcase tests the /login route with correct credentials
    """
    data = {'username': 'jared', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    resp = client.post('/register', json=data, content_type='application/json') # create user
    assert not current_user.is_authenticated

    data={'username': 'jared', 'password_hash': 0xABCD}
    resp = client.post('/login', json=data, content_type='application/json') # log in user
    assert current_user.is_authenticated

    assert resp.status_code == 200
    assert current_user.username == 'jared' # ensure correct user was logged in

def test_login_incorrect_password(client, db):
    """
    This testcase tests the /login route with an incorrect password
    """
    data = {'username': 'jared', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    resp = client.post('/register', json=data, content_type='application/json')
    assert not current_user.is_authenticated

    data={'username': 'jared', 'password_hash': 0xFFFF}
    resp = client.post('/login', json=data, content_type='application/json')

    assert resp.status_code == 401
    assert not current_user.is_authenticated

def test_login_nonexistent_user(client, db):
    """
    This testcase tests the /login route with a nonexistent user
    """
    data={'username': 'jared', 'password_hash': 0xFFFF}
    resp = client.post('/login', json=data, content_type='application/json')
    assert resp.status_code == 401
    assert not current_user.is_authenticated
