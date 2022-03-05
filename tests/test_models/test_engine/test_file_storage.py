#!/usr/bin/python3
"""
Unittest for file_storage([..])
"""
import pep8
import models
import os.path
import unittest
from models import storage
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.engine import file_storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


#F_storage = FileStorage()
#B_model = BaseModel()
#new_classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'Amenity':
#               Amenity, 'Place': Place, 'City': City, 'Review': Review}


class TestFileStorage(unittest.TestCase):
    """ Write unittests for the class FileStorage. """
    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_all(self):
        """ Test that checks the all method. """
        object = storage.all()
        with self.assertRaises(AttributeError):
            print(F_storage.objects)
        with self.assertRaises(AttributeError):
            print(F_storage.file_path)
        self.assertEqual(type(object), dict)
        self.assertEqual(type(F_storage.all()), dict)
        self.assertTrue(hasattr(F_storage, 'all'), True)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertIs(object, storage._FileStorage__objects)

    def test_new(self):
        """ Test that checks the new method. """
        F_storage.new(B_model)
        self.assertTrue(F_storage.all())
        B_model.name = 'Da_Sa'
        self.assertEqual(B_model.name, 'Da_Sa')
        B_model.age = 89
        self.assertEqual(B_model.age, 89)
        self.assertTrue(hasattr(B_model, 'id'))
        self.assertEqual(type(B_model.id), str)
        self.assertTrue(hasattr(storage, 'new'), True)
        self.assertTrue(len(FileStorage.new.__doc__) > 0)
        self.assertEqual(type(B_model), models.base_model.BaseModel)
        with self.assertRaises(AttributeError):
            F_storage.new('string')
        with self.assertRaises(AttributeError):
            F_storage.new(float('nan'))
        with self.assertRaises(AttributeError):
            F_storage.new(float('inf'))

#    def test_save(self):
#        """ Test that checks the save method. """
#        F_storage.new(B_model)
#        F_storage.save()
#        self.assertTrue(os.path.isfile('file.json'))
#        self.assertTrue(hasattr(F_storage, 'save'), True)
#        self.assertEqual(os.path.isfile('file.json'), True)
#        self.assertGreater(B_model.updated_at, B_model.created_at)

#    def test_reload(self):
#        """ Test that checks the reload method. """
#        key = 'BaseModel' + '.' + B_model.id
#        F_storage.new(B_model)
#        F_storage.save()
#        F_storage.reload()
#        self.assertTrue(F_storage.all()[key])
#        self.assertTrue(hasattr(F_storage, 'reload'), True)

    def test_FileStorage_empty(self):
        """ Test that checks the empty FileStorage. """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == '__main__':
    unittest.main()
