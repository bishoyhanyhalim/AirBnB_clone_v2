#!/usr/bin/python3
""" Review module for the airbnb project """
from models.base_model import BaseModel
from sqlalchemy import String, Column, ForeignKey, Integer


class Review(BaseModel):
    """ Review class for store review information for text and place id """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
