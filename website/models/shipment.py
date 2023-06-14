#!/usr/bin/python3

from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(10000))
    sender_address = db.Column(db.String(10000))
    sender_state = db.Column(db.String(10000))
    senders_contact_number = db.Column(db.String(10000))
    sender_city = db.Column(db.String(10000))
    item_name = db.Column(db.String(10000))
    weight = db.Column(db.String(10000))
    recipient_name = db.Column(db.String(10000))
    recipient_address = db.Column(db.String(10000))
    recipient_state = db.Column(db.String(10000))
    recipient_contact_number = db.Column(db.String(10000))
    recipient_city = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
