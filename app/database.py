"""
This module exposes a PyMongo database resource for the application to use
"""
from flask_pymongo import PyMongo

mongo = PyMongo()
