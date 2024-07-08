#!/usr/bin/python3
"""
This file contains the function that starts
the application
"""
from flask import Flask


def create_app():
    """
    This is the function that starts the app and 
    initializes and creates the database
    """

    app = Flask(__name__)
    