#!/usr/bin/python3
"""
Unittest for amenity([..])
"""
import pep8
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

amenity = Amenity()


class TestAmenity(unittest.TestCase):
    """ Write unittests for the class Amenity. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_attr_amenity(self):
        """ Test that checks the amenity class. """
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_amenity(self):
        """ Test that checks the amenity class. """
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
