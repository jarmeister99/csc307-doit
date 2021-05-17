import os, sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

def test_create_task_no_data(client):
    resp = client.post('/tasks',json={})
    assert resp.status_code == 400 # bad request

def test_create_task_success(client, db):
    data = {'name': 'walk the dog', 'description': '', 'dueTime': None}
    resp = client.post('/tasks',json=data)
    assert resp.status_code == 201 # task created successfully
    assert db['tasks'].count_documents({'name': 'walk the dog'}) == 1 #task present in database

def test_create_task_no_name(client, db):
    data = {'name': '', 'description': 'walk the dog', 'dueTime': None}
    resp = client.post('/tasks',json=data)
    assert resp.status_code == 400 # bad request
    assert db['tasks'].count_documents({'name': 'walk the dog'}) == 0 #task not present in database

def test_create_task_bad_data(client):
    data = {'not': 'important', 'a': 'b', 'c': 'd'}
    resp = client.post('/tasks',json=data)
    assert resp.status_code == 400 # bad request

def test_get_two_tasks(client,db):
    data = {'name': 'walk the dog', 'description': '', 'dueTime': None}
    data2 = {'name': 'do the laundry', 'description': '', 'dueTime': None}
    client.post('/tasks',json=data)
    client.post('/tasks',json=data2)
    resp = client.get('/tasks')
    assert resp.status_code == 200 # tasks were gotten


