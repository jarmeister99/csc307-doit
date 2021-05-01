
from app.database import mongo
db = mongo.db

def validate_password(username: str, password_hash: int):
    user = {
        'username': username,
        'password_hash': password_hash
    }
    if (db['users'].count_documents({'username': username, 'password_hash': password_hash}) == 1):
        return True
    else:
        return False


def add_user(username: str, password_hash: int, email: str):
    user = {
        'username': username,
        'password_hash': password_hash,
        'email': email
    }
    if (db['users'].count_documents({'username': username}) == 0):
        db['users'].insert_one(user)
        return True
    else:
        return False

