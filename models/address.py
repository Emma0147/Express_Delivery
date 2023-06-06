#!/usr/bin/python
""" holds class Address"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Address(BaseModel, Base):
    """Representation of a address"""

    __tablename__ = 'addresses'
    address_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", backref="addresses")
    recipient_name = Column(String(100), nullable=False)
    street_address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes address"""
        super().__init__(*args, **kwargs)
