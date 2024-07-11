#!/usr/bin/python3
""" A Database storage class """
from extend import db
from models.comments import Comment
from models.users import User
from models.likes import Like
from models.posts import Post

classes = {
    "User": User,
    "Comment": Comment,
    "Like": Like,
    "Post": Post
}

class DBstorage:
    """ this is a database storage class """
    def check_username_and_email(self, username, email):
        """ check if username and email the user used to sign up exists or not"""
        username = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=email).first()

        if not username and not email:
            return True
        else:
            return False
    
    def create_obj(self, cls, kwargs):
        """ create database objects """
        cls = classes[cls]
        new_user = cls(**kwargs)

        db.session.add(new_user)
        db.session.commit()

        return new_user