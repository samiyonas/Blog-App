#!/usr/bin/python3
""" Likes table """
from extend import db
from models.base_model import BaseModel


class Like(db.Model, BaseModel):
    """ a table for likes """
    id = db.Column(db.String(36), primary_key=True)
    like_count = db.Column(db.Integer())
    user_id = db.Column(db.ForeignKey('user.id'))
    post_id = db.Column(db.ForeignKey('post.id'))