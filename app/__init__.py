"""
This module is responsible for providing a create_app function for Flask to launch from
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv, find_dotenv

from flask import Flask
from flask_cors import CORS

from app.database import mongo
from app.login import login_manager

# factory design pattern
def create_app(db_uri: str):
    """
    This function creates and returns an instance of the Flask app with its own context
    and database URI
    """
    app = Flask(__name__)

    load_dotenv("app.env")
    app.secret_key = os.environ.get('SECRET_KEY')

    # cross origin resource sharing (React <-> Flask)
    CORS(app)

    # initialize mongodb
    app.config['MONGO_URI'] = db_uri
    mongo.init_app(app)

    # initialize login manager
    login_manager.init_app(app)

    # ... here are all the pieces of our program
    with app.app_context():
        # include our routes
        from app.routes import user_routes
        from app.routes import task_routes
        return app

