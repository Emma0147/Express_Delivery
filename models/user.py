#!/usr/bin/python3
""" holds class user """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user"""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    contact_number = Column(String(20), nullable=False)
    email = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    order = relationship("Order", backref="user")
    product = relationship("Product", backref="user")
    shipment = relationship("Shipment", backref="user")

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

    def create_shipment(self, product, start_date, end_date, order):
        """
        Creates a shipment with the specified product,
        dates, order
        """
        from datetime import datetime
        from models.shipment import Shipment
        shipment = Shipment(product=product, order=order,
                          start_date=datetime.strptime(start_date, "%Y-%m-%d"),
                          end_date=datetime.strptime(end_date, "%Y-%m-%d"))
        shipment.save()
        return shipment

    def create_order(self, user_id, items, shipping_address, tracking_info):
        """Creates an order for the specified user"""
        from models.order import Order
        order = Order(
        user_id=user_id,
        items=items,
        shipping_address=shipping_address,
        tracking_info=tracking_info,
        order_status='pending',
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

        if items is not None:
            order.items = items

        if order_date is not None:
            order.order_date = order_date

        order.save()
        return order

    def __setattr__(self, name, value):
        """Sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
