import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app.database import mongo

def test_db_insertion(client, db):
    db['test_users'].insert_one({'name': 'jared'})

# def test_empty_db(client):
#     pass