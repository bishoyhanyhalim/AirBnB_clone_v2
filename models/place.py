#!/usr/bin/python3
""" Place Module for AIRbnb project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.review import Review
from os import getenv
import models
import shlex


class Place(BaseModel, Base):
    """ A place class for user"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete',
                               backref="place")

    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = models.storage.all()
            aray_stro = []
            finally_result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    aray_stro.append(var[key])
            for chars in aray_stro:
                if (chars.place_id == self.id):
                    finally_result.append(chars)
            return (finally_result)
