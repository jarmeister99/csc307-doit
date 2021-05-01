from bson.objectid import ObjectId

from app.login import login_manager
from app.database import mongo
db = mongo.db


class User():
    def add_user(self, username: str, password_hash: int, email: str):
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
    def validate_password(self, username: str, password_hash: int):
        user = {
            'username': username,
            'password_hash': password_hash
        }
        if (db['users'].count_documents({'username': username, 'password_hash': password_hash}) == 1):
            return True
        else:
            return False

@login_manager.user_loader
def load_user(user_id):
    return db['users'].find_one({'_id': ObjectId(id)})




