"""
These testcases cover the /register route which is responsible for creation of new users
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_register_no_data(client):
    """
    This testcase covers the /register route with no payload
    """
    resp = client.post('/register', json={})
    assert resp.status_code == 400 # bad request

def test_register_incorrect_data(client):
    """
    This testcase covers the /register route with an incorrect payload
    """
    data = {'dont_care': 7, 'not_the_right_data': 10}
    resp = client.post('/register', json=data, content_type='application/json')
    assert resp.status_code == 400 # bad request

def test_register_username_success(client, db):
    """
    This testcase covers the /register route with a correct payload and available username
    """
    data = {'username': 'jared', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    resp = client.post('/register', json=data, content_type='application/json')
    assert resp.status_code == 201 # resource created
    assert db['users'].count_documents({'username': 'jared'}) == 1 # resource present in database

def test_register_username_taken(client, db):
    """
    This testcase covers the /register route with a correct payload and unavailble username
    """
    data = {'username': 'taken', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    client.post('/register', json=data, content_type='application/json')
    l1 = db['users'].count_documents({})

    data = {'username': 'taken', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    resp = client.post('/register', json=data, content_type='application/json')
    l2 = db['users'].count_documents({})

    assert resp.status_code == 403 # forbidden request
    assert l1 == l2 # collection length didnt change
