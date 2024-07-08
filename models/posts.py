#!/usr/bin/python3
from extend import db
from uuid import uuid4
from models.base_model import BaseModel


class Post(db.Model, BaseModel):
    """ a post table """
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    title = db.Column(db.Text)
    subtitle = db.Column(db.String(1024))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    user_id = db.Column(db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post', cascade='all, delete')
    likes = db.relationship('Like', backref='post', cascade='all, delete')