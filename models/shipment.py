#!/usr/bin/python
""" holds class Shipment"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.order import Order
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime


class Shipment(BaseModel, Base):
    """Representation of a shipment"""

    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    order_id = Column(String(60), ForeignKey('order.id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    tracking_number = Column(String(50), nullable=False)
    status = Column(Enum('in_transit', 'out_for_delivery', 'delivered'), nullable=False)
    order = relationship("Order")

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

