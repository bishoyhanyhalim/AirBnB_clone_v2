from unittest import TestCase
from unittest.mock import patch
import unittest
from io import StringIO
from console import HBNBCommand
from os import getenv


class TestHBNBCommand(TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "Testing DBstorage")
    def test_create_kwargs(self):
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
