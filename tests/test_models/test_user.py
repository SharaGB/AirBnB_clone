#!/usr/bin/python3
"""
Unittest for user([..])
"""
import pep8
import unittest
from models.user import User
from models.base_model import BaseModel

user = User()


class TestUser(unittest.TestCase):
    """ Write unittests for the class User. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attr_User(self):
        """ Test that checks the User class. """
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, '')
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, '')
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, '')
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, '')

    def test_User(self):
        """ Test that checks the User class. """
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
