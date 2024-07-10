#!/usr/bin/python3
""" the app file and the list of blueprints """
from __init__ import create_app
from api.home import hpage


app = create_app()

app.secret_key = "hellowbitches"

app.register_blueprint(hpage)

if __name__ == "__main__":
    app.run(debug=True)
