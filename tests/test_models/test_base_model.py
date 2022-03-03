#!/usr/bin/python3
""""""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class test_base(unittest.TestCase):
    """"""
    def test_init(self):
        """Test the init of BaseModel"""
        instance = BaseModel()
        self.assertEqual(type(instance), BaseModel)
        instance.name = 'Clone'
        self.assertEqual(instance.name, 'Clone')
        instance.my_number = 2022
        self.assertEqual(instance.my_number, 2022)
        self.assertEqual(type(instance.id), str)
        self.assertEqual(type(instance.created_at), datetime)


if __name__ == '__main__':
    unittest.main()
