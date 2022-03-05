#!/usr/bin/python3
""""""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_base(unittest.TestCase):
    """Group of tests to probe the BaseModel behavior."""
    @classmethod
    def setUpClass(cls):
        """Set up the class."""
        cls.instance = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Final step."""
        del cls.instance

    def test_doc(self):
        """Test the documentation of BaseModel."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_base_attr(self):
        """Test the BaseModel attributes."""
        self.instance.name = 'Clone'
        self.instance.my_number = 2022
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(self.instance.id)
        self.assertIsInstance(self.instance.id, str)
        self.assertTrue(self.instance.created_at)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertTrue(self.instance.updated_at)
        self.assertIsInstance(self.instance.updated_at, datetime)
        self.assertIsNotNone(self.instance.id)
        self.assertEqual(self.instance.name, 'Clone')
        self.assertEqual(self.instance.my_number, 2022)

    def test_save(self):
        """Test the save method."""
        past_update = self.instance.updated_at
        self.instance.save()
        self.assertIsNot(self.instance.created_at, self.instance.updated_at)
        self.assertIsNot(past_update, self.instance.updated_at)

    def test_to_dict(self):
        """Test the dict method."""
        new = BaseModel()
        new.name = "School"
        new.my_number = 2020
        dictionary = new.to_dict()
        attr = [
            "id",
            "created_at",
            "updated_at",
            "name",
            "my_number",
            "__class__"
        ]
        self.assertCountEqual(dictionary.keys(), attr)
        self.assertIn('id', dictionary.keys())
        self.assertIn('created_at', dictionary.keys())
        self.assertIn('updated_at', dictionary.keys())
        self.assertIn('name', dictionary.keys())
        self.assertIn('my_numbers', dictionary.keys())
        self.assertIn('__class__', dictionary.keys())
        self.assertEqual(dictionary['name'], "School")
        self.assertIs(type(dictionary['name']), str)
        self.assertEqual(dictionary['my_number'], 2020)
        self.assertIs(type(dictionary['my_number']), int)


if __name__ == '__main__':
    unittest.main()
