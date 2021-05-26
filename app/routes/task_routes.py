from flask_login.utils import login_required
from app.models.tasks import Task
from flask.globals import current_app as app
from flask import request
import flask_login

from app.database import mongo

@app.route('/tasks', methods=['GET','POST'])
@login_required
def tasks_route():
    if request.method == 'POST': 
        #save task
        if not request.json:
            return {}, 400
        if request.json.get('name') is None or request.json.get('name') == '':
            #not checking description to allow empty description
            return {},400
        #save task here  
        Task.create_task(name=request.json['name'],description=request.json['description'],userId=flask_login.current_user.get_id())
        return {}, 201
    elif request.method == 'GET':
        #show all tasks
        tasks = Task.get_all_by_user(user_id=flask_login.current_user.get_id())
        return tasks, 200
        


