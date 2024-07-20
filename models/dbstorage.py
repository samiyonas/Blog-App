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
    
    def number_of_users(self):
        """ get the total number of users of the blog """
        user_count = User.query.count()

        return user_count
    
    def get_all_users(self):
        """ get all users of the blog """
        user_list = []
        users = User.query.all()
        for i in users:
            user = {
                "id": i.id,
                "name": i.name,
                "username": i.username,
                "email": i.email
            }
            user_list.append(user)
        return user_list
    
    def get_user_id(self, user_id):
        """ get a specific user """
        user = User.query.filter_by(id=user_id).first()
        if user:
            user_dict = {
                "name": user.name,
                "username": user.username,
                "email": user.email
            }
            return user_dict
        return {"error": "user not found"}
    
    def get_post_id(self, post_id):
        """ get a specific post """
        post = Post.query.filter_by(id=post_id).first()
        if post:
            post_dict = {
                "title": post.title,
                "subtitle": post.subtitle,
                "content": post.content
            }
            return post_dict
        return {"error": "post not found"}
    
    def get_comment_user(self, user_id):
        """ get all comments made by specific user """
        all_comments = []
        comments = Comment.query.filter_by(user_id=user_id).all()
        if comments:
            for i in comments:
                comment = {
                    "post_id": i.post_id,
                    "content": i.content
                }
                all_comments.append(comment)
            return all_comments
        return {"error": "this user hasn't commented yet"}
    
    def get_comment_post(self, post_id):
        """ get all comments under a specific post """
        all_comments = []
        comments = Comment.query.filter_by(post_id=post_id).all()
        if comments:
            for i in comments:
                comment = {
                    "user_id": i.user_id,
                    "content": i.content
                }
                all_comments.append(comment)
            return all_comments
        return {"error": "no comments under this post"}