#!/usr/bin/python3
""" the app file and the list of blueprints """
from __init__ import create_app
from api.home import hpage
from api.client import client
from os import getenv
from dotenv import load_dotenv


load_dotenv()

app = create_app()

app.secret_key = getenv('SECRET_KEY')

app.register_blueprint(hpage)
app.register_blueprint(client)

if __name__ == "__main__":
    app.run(debug=True)
