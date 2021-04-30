import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json

from app import app

app = app.test_client()
resp = app.post('/register', json={}, content_type='application/json')


# resp = app.get('http://127.0.0.1:5000/register', json={})
print(resp)