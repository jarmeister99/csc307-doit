from app import app

@app.route('/login')
def login_route(methods=['GET', 'POST']):
    return 'Login route'

@app.route('/register')
def register_route(methods=['GET', 'POST']):
    return 'Register route'