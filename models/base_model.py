#!/usr/bin/python3
""" User table """
from datetime import datetime


class BaseModel:
    """ the base model that all the other classes inherit from """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if "created_at" in dir(self):
            setattr(self, "created_at", datetime.now())
        if "updated_at" in dir(self):
            setattr(self, "updated_at", datetime.now())
