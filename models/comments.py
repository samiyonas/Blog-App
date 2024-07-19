#!/usr/bin/python3
""" Comments table """
from uuid import uuid4
from extend import db
from models.base_model import BaseModel
from datetime import datetime


class Comment(db.Model, BaseModel):
    """ a table for comments """
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    content = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey('user.id'))
    post_id = db.Column(db.ForeignKey('post.id'))
