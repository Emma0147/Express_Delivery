#!/usr/bin/python
""" holds class Order"""
import models
from models.base_model import BaseModel, Base
from models.product import Product
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime


class Order(BaseModel, Base):
    """Representation of a order"""

        __tablename__ = 'orders'
        order_id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        user = relationship("User", backref="orders")
        product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
        product = relationship("Products", backref="orders")
        shipping_address_id = Column(Integer, ForeignKey('addresses.id'), nullable=False)
        shipping_address = relationship("Address")
        order_status = Column(String(50), nullable=False)
        created_at = Column(DateTime, nullable=False)
        updated_at = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes order"""
        super().__init__(*args, **kwargs)
