#!/usr/bin/python3
"""
This file contains the function that starts
the application
"""
from flask import Flask
from extend import db


def create_app():
    """
    This is the function that starts the app and 
    initializes and creates the database
    """

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://user_blog:passwd@localhost/db_blog"
    app.config['SQLALCHEMY_TRACK_MODFICATION'] = False

    with app.app_context():
        """ wrapped in app_context so flask thinks the application was initialized"""
        from models.comments import Comment
        from models.posts import Post
        from models.users import User

        db.init_app(app)
        db.create_all()

        return app   