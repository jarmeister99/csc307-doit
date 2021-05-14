import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_db_insertion(db):
    db['users'].insert_one({'name': 'jared'})
    assert db['users'].count_documents({}) == 1

    db['todos'].insert_one({'title': 'clean fish tank'})
    assert db['todos'].count_documents({}) == 1

def test_empty_db(db):
    assert db['users'].count_documents({}) == 0
    assert db['todos'].count_documents({}) == 0
