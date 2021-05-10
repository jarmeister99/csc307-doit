"""
This file provides test fixtures to be used in the testing of the DO IT web application backend
"""

import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# pylint: disable=C0413
# Disable import must be placed at top of the module warning.
# ... path must be appended before attempting to import app
from app import create_app
from app.database import mongo

# pylint: disable=W0621
# Disable redefinined name from outer scope warning.
# ... fixture name must be app for pytest base fixtures to work properly
@pytest.fixture()
def db(app):
    """
    This fixture provides an empty test database to be used in testcases
    """
    # pylint: disable=W0613
    # Disable unusued argument warning.
    # ... app is a fixture with side effects not directly seen in this scope
    for collection in mongo.db.list_collection_names():
        mongo.db.drop_collection(collection)
    return mongo.db

@pytest.fixture(scope='session')
def app():
    """
    This fixture provides a test application using a test database
    """
    return create_app('mongodb://localhost:27017/test_doit')
