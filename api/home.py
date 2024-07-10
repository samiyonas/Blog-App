#!/usr/bin/python3
""" Blueprint of the app """
from flask import Blueprint, render_template, request, session
from extend import db
from models.users import User


hpage = Blueprint(
    'hpage',
    __name__,
    url_prefix="/home",
    template_folder="templates",
    static_folder="static"
)

@hpage.route("/", methods=['GET'])
def home():
    """ Render the home page """
    return render_template("home.html")

@hpage.route("/signup", methods=['GET', 'POST'])
def signup():
    """ the sign up page will be rendered """
    if request.method == 'POST':
        data = request.get_json()
        if data:
            name = data.get("name")
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            new_user = User(
                name=name,
                username=username,
                email=email,
                password=password
            )
            
            db.session.add(new_user)
            db.session.commit()
    elif request.method == 'GET':
        return render_template("signup.html")
    