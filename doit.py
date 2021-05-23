"""
This module provides an entry point for Flask to launch the web application
"""

from app import create_app
app = create_app('mongodb://localhost:27017/doit')
