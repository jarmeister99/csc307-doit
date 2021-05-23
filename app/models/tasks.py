import uuid
from bson.objectid import ObjectId
from app.database import mongo
from bson.json_util import dumps

class Task():
    def __init__(self, name, description, dueTime, userId=None, _id=None):
        self.name=name
        self.description = description
        self.dueTime = dueTime
        self.userId = userId
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_id(cls,_id):
        data = mongo.db['tasks'].find_one({'_id': _id})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_all(cls):
        cur = mongo.db['tasks'].find()
        list_cur = list(cur)
        data = dumps(list_cur)
        return data
        
    @classmethod
    def create_task(cls, name, userId, description=None, dueTime=None):
        #if task is None:
        new_task = cls(name, description, dueTime,userId)
        new_task.save_to_db()
        return True
    

    def json(self):
        return {
            '_id': self._id,
            'userId': self.userId,
            'name': self.name,
            'description': self.description,
            'dueTime': self.dueTime
        }
    
    def save_to_db(self):
        mongo.db['tasks'].insert_one(self.json())