#!/usr/bin/python3
""" Review module for the airbnb project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for store review information for text and place id """
    text = ""
    place_id = ""
    user_id = ""
