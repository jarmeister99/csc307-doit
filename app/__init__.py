import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv, find_dotenv

from flask import Flask
from flask_cors import CORS

from app.database import mongo
from app.login import login_manager

# factory design pattern
def create_app(db_uri: str):
    app = Flask(__name__)

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(BASEDIR, '.env'), verbose=True)

    x = os.getenv("SECRET_KEY")
    print(x)

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

if __name__ == '__main__':
    app = create_app('mongodb://localhost:27017/doit')
    # app.run()


