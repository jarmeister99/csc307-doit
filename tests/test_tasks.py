"""
These testcases cover the /tasks route which is responsible for creating, modifying, deleting,
and retrieving todo-list tasks
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bson.objectid import ObjectId
from flask_login import current_user
from app.models.tasks import Task
from app.models.users import User


def test_create_task_no_data(client):
    """
    This testcase tests the /tasks POST route with an empty payload
    """
    resp = client.post('/tasks',json={})
    assert resp.status_code == 400 # bad request

def test_create_task_success(client, db):
    """
    This testcase tests the /tasks POST route with a correct payload
    """
    data = {'username': 'jared', 'password_hash': 0xABCD, 'email': 'email@address.com'}
    resp = client.post('/register', json=data, content_type='application/json') # create user

    data={'username': 'jared', 'password_hash': 0xABCD}
    resp = client.post('/login', json=data, content_type='application/json') # log in user

    assert current_user.is_authenticated

    data = {'name': 'walk the dog', 'description': '', 'dueTime': None}
    resp = client.post('/tasks',json=data)
    assert resp.status_code == 201 # task created successfully
    assert db['tasks'].count_documents({'name': 'walk the dog'}) == 1 #task present in database

def test_create_task_no_name(client, db):
    """
    This testcase tests the /tasks POST route without providing a name
    """
    data = {'name': '', 'description': 'walk the dog', 'dueTime': None}
    resp = client.post('/tasks',json=data)
    assert resp.status_code == 400 # not logged in
    assert db['tasks'].count_documents({'name': 'walk the dog'}) == 0 #task not present in database

def test_create_task_bad_data(client):
    """
    This testcase tests the /tasks POST route with an incorrect payload
    """
    data = {'not': 'important', 'a': 'b', 'c': 'd'}
    resp = client.post('/tasks',json=data)
    assert resp.status_code == 400 # not logged in

def test_get_two_tasks(client, db):
    """
    This testcase tests the /tasks GET route with two entries in th edb
    """
    data = {'name': 'walk the dog', 'description': '', 'dueTime': None}
    data2 = {'name': 'do the laundry', 'description': '', 'dueTime': None}
    client.post('/tasks',json=data)
    client.post('/tasks',json=data2)
    resp = client.get('/tasks')
    assert resp.status_code == 200 # tasks were gotten
