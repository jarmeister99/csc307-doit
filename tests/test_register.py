import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

def test_register_no_data(client):
    resp = client.post('/register', json={})
    assert(resp.status_code == 400) # bad request

def test_register_incorrect_data(client):
    data = {'dont_care': 7, 'not_the_right_data': 10}
    resp = client.post('/register', json=data, content_type='application/json')
    assert(resp.status_code == 400) # bad request 




