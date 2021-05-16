from flask.globals import current_app as app
from flask import request

from app.database import mongo

@app.route('/tasks', methods=['GET','POST'])
def tasks_route():
    if request.method == 'POST': 
        #save task
        if not request.json:
            return {}, 400
        if request.json.get('name') is None:
            #not checking description to allow empty description
            return {},400
        #save task here    
        return {}, 200

