#!/usr/bin/python
""" holds class Shipment"""
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db
from sqlalchemy import Column, String, ForeignKey, DateTime


class Shipment(BaseModel, Base):
    """Representation of a shipment"""

    __tablename__ = 'shipments'
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

    def __init__(self, *args, **kwargs):
        """Initializes shipment"""
        super().__init__(*args, **kwargs)

    @property
    def state(self):
        """loads status options"""
        return self.status

    @state.setter
    def state(self, value):
        """sets status"""
        options = ["in_transit", "out_for_delivery", "delivered"]
        if value in options:
            self.state = value

