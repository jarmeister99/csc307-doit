"""
These testcases cover the db fixture used for testing
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.tasks import Task
from app.models.users import User

def test_get_task_by_id(db):
    """
    This testcase tests the Task() get_by_id() method
    """
    task = Task('task', 'description', 'time', userId='user', _id='dummy_id')
    task.save_to_db()
    task = Task.get_by_id('dummy_id')
    assert task.userId == 'user'

def test_get_user_by_email(db):
    """
    This testcase tests the User() get_user_by_email() method
    """
    user = User(username='jared', email='email', password_hash='ABCD', _id='id123')
    user.save_to_db()
    user = User.get_by_email(email='email')
    assert user.username == 'jared'

def test_db_insertion(db):
    """
    This testcase ensures that users can be inserted and counted in the test database
    """
    db['users'].insert_one({'name': 'jared'})
    assert db['users'].count_documents({}) == 1

    db['todos'].insert_one({'title': 'clean fish tank'})
    assert db['todos'].count_documents({}) == 1

def test_empty_db(db):
    """
    This tetscase ensures that the fixture db resets its contents on every use
    """
    assert db['users'].count_documents({}) == 0
    assert db['todos'].count_documents({}) == 0
