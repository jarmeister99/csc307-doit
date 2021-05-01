import uuid
from bson.objectid import ObjectId

from app.login import login_manager
from app.database import mongo
db = mongo.db


class User():
    def __init__(self, username, email, password_hash, _id=None):

        self.username = username
        self.email = email
        self.password_hash = password_hash
        self._id = uuid.uuid4().hex if _id is None else _id

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return True
    def get_if(self):
        return self._id

    @classmethod
    def get_by_username(cls, username):
        data = db['users'].find_one({'username': username}) 
        if data is not None:
            return cls(**data)
        
    @classmethod
    def get_by_email(cls, email):
        data = db['users'].find_one({'email': email}) 
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = db['users'].find_one({'_id': _id}) 
        if data is not None:
            return cls(**data)

    @classmethod
    def register_user(cls, username: str, password_hash: int, email: str):
        user = cls.get_by_username(username)
        if user is None:
            new_user = cls(username, email, password_hash)
            new_user.save_to_db()
            return True
        return False

    @staticmethod
    def login_user(username: str, password_hash: int):
        user = User.get_by_username(username)
        if user is not None:
            return user.password_hash == password_hash
        return False

    def json(self):
        return {
            '_id': self._id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash
        }

    def save_to_db(self):
        db['users'].insert_one(self.json())

@login_manager.user_loader
def load_user(user_id):
    return db['users'].find_one({'_id': ObjectId(user_id)})




