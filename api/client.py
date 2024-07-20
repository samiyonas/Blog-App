#!/usr/bin/python3
from flask import Blueprint, jsonify
from models.dbstorage import DBstorage


storage = DBstorage()


client = Blueprint(
    "client",
    __name__,
    url_prefix="/api/client"
)

@client.route("/number_of_users", methods=['GET'], strict_slashes=False)
def number_of_users():
    """ return the number of users of this blog """
    user_count = storage.number_of_users()

    return jsonify({"user_count": user_count})

@client.route("/users", methods=['GET'], strict_slashes=False)
def users():
    """ get all users """
    all_users = storage.get_all_users()
    
    return jsonify(all_users)

@client.route("/user/<id>", methods=['GET'], strict_slashes=False)
def user(id):
    """ get a specific user """
    one_user = storage.get_user_id(id)

    return jsonify(one_user)

@client.route("/post/<id>", methods=['GET'], strict_slashes=False)
def post(id):
    """ get a specific post """
    one_post = storage.get_post_id(id)

    return jsonify(one_post)

@client.route("/user_comment/<user_id>", methods=['GET'], strict_slashes=False)
def user_comment(user_id):
    """ get all comments made by a specific user """
    all_comments = storage.get_comment_user(user_id)

    return jsonify(all_comments)

@client.route("/post_comment/<post_id>", methods=['GET'], strict_slashes=False)
def post_comment(post_id):
    """ get all comments under a specific post """
    all_comments = storage.get_comment_post(post_id)

    return jsonify(all_comments)
