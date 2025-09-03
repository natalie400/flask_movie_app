from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import models
@app.route("/")


def home():
    return "Flask Note App with Database is running!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
