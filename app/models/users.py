
from app.database import mongo
db = mongo.db

def add_user(username: str, password_hash: int, email: str):
    # build user
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


