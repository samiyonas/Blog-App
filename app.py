#!/usr/bin/python3
""" the app file and the list of blueprints """
from __init__ import create_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
