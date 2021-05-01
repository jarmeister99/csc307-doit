import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app.database import mongo

def test_db_insertion(client, db):
    db['users'].insert_one({'name': 'jared'})
    assert(db['users'].count_documents({}) == 1)

def test_empty_db(client, db):
    assert(db['users'].count_documents({}) == 0)