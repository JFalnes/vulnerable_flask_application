# Author:        F4lnes
# Created        12.03.2021
from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Products(db.Model):
    item_no = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    qty = db.Column(db.Integer)
    price = db.Column(db.String(1000))
