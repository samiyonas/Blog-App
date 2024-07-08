#!/usr/bin/python3
""" Users table """
from extend import db
from uuid import uuid4
from models.base_model import BaseModel


class User(db.Model, BaseModel):
    """ a User table """
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(16), nullable=False)
    posts = db.relationship('Post', backref='user', cascade='all, delete')
    comments = db.relationship('Comment', backref='user', cascade='all, delete')
    likes = db.relationship('Like', backref='user', cascade='all, delete')
