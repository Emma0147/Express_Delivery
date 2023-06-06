#!/usr/bin/python
""" holds class Product"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5


class Product(BaseModel, Base):
    """Representation of a product"""

    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(128), nullable=False)
    product_description = Column(String(255))
    product_weight = Column(String(128), nullable=False)
    product_dimension = Column(String(128), nullable=False)
    order = relationship("Order", backref="products")
    shipments = relationship("Shipment", backref="products")
    order_id = Column(String(60), ForeignKey('orders.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes order"""
        super().__init__(*args, **kwargs)

    def accept_order(self, order):
        """Accepts the specified order"""
        order.status = 'accepted'
        order.save()

    def reject_order(self, order):
        """Rejects the specified order"""
        order.status = 'rejected'
        order.save()
