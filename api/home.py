#!/usr/bin/python3
""" Blueprint of the app """
from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
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
    random_posts = storage.random_posts()
    return render_template("home.html", form=form, random_posts=random_posts)

@hpage.route('/login', methods=['POST'])
def login():
    """ the login logic """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = storage.login_credentials(username, password)
        if user:
            session["user"] = {
                'id': user.id,
                'name': user.name,
                'username': user.username
            }
            return redirect(url_for('hpage.pfpage'))
        else:
            return redirect(url_for('hpage.home'))
        
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

@hpage.route("/pfpage", methods=['GET', 'POST', 'PUT'], strict_slashes=False)
def pfpage():
    if session:
        name = session["user"]["name"]
        username = session["user"]["username"]
        random_posts = storage.random_posts()
        
        return render_template(
            "pfpage.html",
            name=name,
            username=username,
            random_posts=random_posts
        )
    
@hpage.route("/post", methods=['POST'], strict_slashes=False)
def post():
    if session:
        data = request.json
        if data:
            data.update({"user_id": session["user"]["id"]})
            post = storage.create_obj("Post", data)
            return jsonify({"message": "Post added successfully"})
    return jsonify({"message": "you have to login first"})

@hpage.route("/reading_page", methods=['GET', 'POST'], strict_slashes=False)
def reading_page():
    """ render the reading page """
    data = request.get_json()
    if data:
        title = data.get("title")
        subtitle = data.get("subtitle")
        content = data.get("content")
        
        if not title or not subtitle or not content:
            return jsonify({"message": "Missing field"}), 400
        rendered =  render_template(
            "reading_page.html",
            title=title,
            subtitle=subtitle,
            content=content
        )
        return jsonify({"html": rendered})
    return jsonify({"message": "error while changing to dictionary"}), 400

@hpage.route("/update_user", methods=['PUT'], strict_slashes=False)
def update_user():
    """ update the user info """
    if session:
        data = request.json

        if data:
            data.update({"id": session["user"]["id"]})
            storage.update_user(data)
    return jsonify({"error": "message"}), 400

@hpage.route("/comment", methods=['POST'], strict_slashes=False)
def comment():
    """ the comments posted """
    if session:
        user_id = session["user"]["id"]
        data = request.json
        if data:
            data.update({"user_id": user_id})
            if storage.create_obj('Comment', data):
                return jsonify({"message": "no error"})
        return jsonify({"message": "incorrect data"})

@hpage.route("/logout", methods=['GET'], strict_slashes=False)
def logout():
    session.clear()
    return redirect(url_for("hpage.home"))