#!/usr/bin/python3
"""
Unittest for city([..])
"""
import pep8
import unittest
from models.city import City
from models.base_model import BaseModel

city = City()


class TestCity(unittest.TestCase):
    """ Write unittests for the class City. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_attr_City(self):
        """ Test that checks the City class. """
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, '')
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, '')

    def test_City(self):
        """ Test that checks the City class. """
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
