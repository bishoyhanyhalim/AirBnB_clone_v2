#!/usr/bin/python3
""" Review module for the airbnb project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Review(BaseModel, Base):
    """ Review class for store review information about review places """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
