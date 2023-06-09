#!/usr/bin/python3
""" holds class user """

import models
from models.base_model import BaseModel, Base
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user"""

    __tablename__ = 'users'
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

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)
