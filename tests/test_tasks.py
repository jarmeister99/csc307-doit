"""
These testcases cover the /tasks route which is responsible for creating, modifying, deleting,
and retrieving todo-list tasks
"""
from json import loads
import os
import sys

from flask_login import current_user

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.tasks import Task

def login_a(c):
    """
    auto login function
    """
    data = {'username': 'jared', 'password_hash': 0xABCD,
            'email': 'email@address.com'}
    resp = c.post('/register', json=data,
                       content_type='application/json')  # create user

    data = {'username': 'jared', 'password_hash': 0xABCD}
    resp = c.post('/login', json=data,
                       content_type='application/json')  # log in user
    assert current_user.is_authenticated

    return resp


def test_create_task_no_data(client):
    """
    This testcase tests the /tasks POST route with an empty payload
    """
    login_a(client)
    resp = client.post('/tasks', json={})
    assert resp.status_code == 400  # bad request


def test_create_task_success(client,db):
    """
    This testcase tests the /tasks POST route with a correct payload
    """
    login_a(client)

    data = {'name': 'walk the dog', 'description': '', 'dueTime': None}
    resp = client.post('/tasks', json=data)
    assert resp.status_code == 201  # task created successfully
    assert db['tasks'].count_documents(
        {'name': 'walk the dog'}) == 1  # task present in database


def test_delete_task_success(client,db):
    """
    This testcase tests the /tasks POST route with a correct payload
    """
    login_a(client)
    data = {'name': 'walk the dog', 'description': '', 'dueTime': None,
    '_id': '60b081d17e1496d85e2b98db'}
    resp = client.post('/tasks', json=data)
    assert resp.status_code == 201  # task created successfully
    assert db['tasks'].count_documents(
        {'name': 'walk the dog'}) == 1  # task present in database
    resp = client.delete('/tasks/60b081d17e1496d85e2b98db')
    #assert db['tasks'].count_documents({'name': 'walk the dog'})==0


def test_create_task_no_name(client, db):
    """
    This testcase tests the /tasks POST route without providing a name
    """
    login_a(client)

    print("nonametest", file=sys.stderr)
    data = {'name': '', 'description': 'walk the dog', 'dueTime': None}
    resp = client.post('/tasks', json=data)
    assert resp.status_code == 400  # not logged in
    assert db['tasks'].count_documents(
        {'name': 'walk the dog'}) == 0  # task not present in database


def test_create_task_bad_data(client):
    """
    This testcase tests the /tasks POST route with an incorrect payload
    """
    login_a(client)

    data = {'not': 'important', 'a': 'b', 'c': 'd'}
    resp = client.post('/tasks', json=data)
    assert resp.status_code == 400  # not logged in


def test_get_two_tasks(client):
    """
    This testcase tests the /tasks GET route with two entries in the db
    """
    login_a(client)

    data = {'name': 'walk the dog', 'description': '', 'dueTime': None}
    data2 = {'name': 'do the laundry', 'description': '', 'dueTime': None}
    client.post('/tasks', json=data)
    client.post('/tasks', json=data2)
    resp = client.get('/tasks')
    assert resp.status_code == 200  # tasks were gotten

def test_user_creates_task(client, db):
    """
    This testcase tests the /tasks POST and /tasks GET route with specific user data
    """
    login_a(client)

    data = {'name': 'walk the dog', 'description': 'two blocks', 'dueTime': None}
    client.post('/tasks', json=data)
    resp = client.get('/tasks')
    assert resp.status_code == 200

    tasks = loads(resp.data)
    t = tasks[0]

    assert t.get('userId') == current_user.get_id()
    assert t.get('name') == 'walk the dog'

def test_get_all_tasks(client, db):
    """
    This testcase tests the /tasks POST route and uses Tasks.get_all() to ensure data was posted
    """
    login_a(client)
    data = {'name': 'walk the dog', 'description': 'two blocks', 'dueTime': None}
    client.post('/tasks', json=data)
    resp = client.get('/tasks')
    assert resp.status_code == 200

    tasks = Task.get_all()
    task_data = loads(tasks)

    assert len(task_data) == 1

    assert task_data[0].get('name') == 'walk the dog'
