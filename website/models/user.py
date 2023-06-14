#!/usr/bin/python3

from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    contact_number = db.Column(db.String(150))
    state = db.Column(db.String(150))
    city = db.Column(db.String(150))
    address = db.Column(db.String(150))
    password = db.Column(db.String(150))
    shipments = db.relationship('Shipment')
