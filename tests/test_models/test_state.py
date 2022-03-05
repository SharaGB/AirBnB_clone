#!/usr/bin/python3
"""
Unittest for state([..])
"""
import pep8
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel

state = State()
created_at = datetime.now()
updated_at = datetime.now()


class TestState(unittest.TestCase):
    """ Write unittests for the class State. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attr_State(self):
        """ Test that checks the State class. """
        self.assertIs(type(state), State)
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')

    def test_State(self):
        """ Test that checks the State class. """
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
