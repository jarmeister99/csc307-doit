from flask import Flask

app = Flask(__name__)

from app.routes import user_routes
from app.routes import view_routes

if __name__ == '__main__':
    app.run()