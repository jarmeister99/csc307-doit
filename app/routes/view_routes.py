from flask.globals import current_app as app

@app.route('/')
def index():
    return 'Home Page'