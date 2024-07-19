#!/usr/bin/python3
""" A Database storage class """
from extend import db
from models.comments import Comment
from models.users import User
from models.posts import Post


classes = {
    "User": User,
    "Comment": Comment,
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
        new_obj = cls(**kwargs)

        db.session.add(new_obj)
        db.session.commit()

        return new_obj
    
    def login_credentials(self, username, password):
        """ check login credentials """
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        else:
            return False
    
    def random_posts(self):
        """ fetch random posts """
        posts = []
        all_posts = Post.query.all()
        if len(all_posts) < 1:
            return posts
        for i in range(10):
            if i < len(all_posts):
                posts.append({
                    "title": all_posts[i].title,
                    "subtitle": all_posts[i].subtitle,
                    "content": all_posts[i].content,
                    "id": all_posts[i].id,
                })
            else:
                break
        return posts
    
    def delete_obj(self, cls, id):
        """ delete an object """
        user = cls.query.filter_by(id=id)

        db.session.delete(user)
        db.session.commit()

    def update_user(self, data):
        """ update a user """
        user = User.query.filter_by(id=data.get('id')).first()
        user.name = data.get('name')
        user.username = data.get('username')

        db.session.commit()
    