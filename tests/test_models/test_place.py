#!/usr/bin/python3
"""
Unittest for place([..])
"""
import pep8
import unittest
from models.place import Place
from models.base_model import BaseModel

place = Place()


class TestPlace(unittest.TestCase):
    """ Write unittests for the class place. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_attr_place(self):
        """ Test that checks the place class. """
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, '')
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, '')
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, '')
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, '')
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(place.amenity_ids, [])

    def test_place(self):
        """ Test that checks the place class. """
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
