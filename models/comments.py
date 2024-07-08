#!/usr/bin/python3
""" Comments table """
from extend import db
from models.base_model import BaseModel
from datetime import datetime


class Comment(db.Model, BaseModel):
    """ a table for comments """
    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    content = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey('user.id'))
    post_id = db.Column(db.ForeignKey('post.id'))
