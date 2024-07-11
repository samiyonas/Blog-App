#!/usr/bin/python3
""" Blueprint of the app """
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models.dbstorage import DBstorage
from form import LoginForm, RegisterForm


storage = DBstorage()

hpage = Blueprint(
    'hpage',
    __name__,
    url_prefix="/home",
    template_folder="templates",
    static_folder="static"
)

@hpage.route("/", methods=['GET'], strict_slashes=False)
def home():
    """ Render the home page """
    form = LoginForm()
    return render_template("home.html", form=form)

@hpage.route("/signup", methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """ the sign up page will be rendered """
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        if storage.check_username_and_email(username, email):
            form_dict = form.to_dict()
            user = storage.create_obj('User', form_dict)
            session["user"] = {
                'id': user.id,
                'name': user.name,
                'username': user.username
            }
            return redirect(url_for('hpage.pfpage'))
        else:
            flash("Invalid username or email")
    return render_template("signup.html", form=form)

@hpage.route("/pfpage", methods=['GET, POST', 'PUT'], strict_slashes=False)
def pfpage():
    if session:
        
