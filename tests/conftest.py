import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import create_app

@pytest.fixture(scope='session')
def app():
    app = create_app('mongodb://localhost:27017/test_doit')
    return app
