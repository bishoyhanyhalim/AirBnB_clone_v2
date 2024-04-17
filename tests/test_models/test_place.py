#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from io import StringIO
from unittest.mock import patch
import unittest
import models
from models.engine.db_storage import DBStorage


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipIf(type(models.storage) == DBStorage, "")
    def test_create_kwargs(self):
        self.console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as out:
            in_put = ('create Place city_id="0001" user_id="0001" '
                      'name="My_little_house" '
                      'number_rooms=4 number_bathrooms=2 max_guest=10 '
                      'price_by_night=300 '
                      'latitude=b longitude=-122.431297')
            self.console.onecmd(in_put)
            out_create = out.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out:
            self.console.onecmd("all Place")
            out_all = out.getvalue()
            self.assertIn(out_create, out_all)
            self.assertIn("'city_id': '0001'", out_all)
            self.assertIn("'user_id': '0001'", out_all)
            self.assertIn("'number_bathrooms': 2", out_all)
            self.assertIn("'price_by_night': 300", out_all)
            self.assertIn("'name': 'My little house'", out_all)
            self.assertIn("'max_guest': 10", out_all)
            self.assertIn("'number_rooms': 4", out_all)
            self.assertIn("'longitude': -122.431297", out_all)
            self.assertNotIn("'latitude': b", out_all)
