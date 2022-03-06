#!/usr/bin/python3
"""
Unittest for file_storage([..])
"""
import pep8
import models
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

F_storage = FileStorage()
B_model = BaseModel()
object = storage.all()


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
        self.assertNotEqual(object, {})
        with self.assertRaises(AttributeError):
            print(F_storage.objects)
        with self.assertRaises(AttributeError):
            print(self.F_storage.__file_path)
        self.assertEqual(type(object), dict)
        self.assertTrue(hasattr(F_storage, 'all'), True)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertIs(object, storage._FileStorage__objects)

# class TestFileStorage(unittest.TestCase):
#     """ Write unittests for the class FileStorage. """

#     @classmethod
#     def setUpClass(cls):
#         """Set up class."""
#         # cls.F_storage = FileStorage()
#         # cls.B_model = BaseModel()
#         # cls.object = storage.all()

#     def test_pep8_conformance(self):
#         """ Test that we conform to PEP8. """
#         pep8style = pep8.StyleGuide(quiet=True)
#         result = pep8style.check_files(['models/engine/file_storage.py'])
#         self.assertEqual(result.total_errors, 0,
#                          "Found code style errors (and warnings).")

    # def test_all(self):
    #     """ Test that checks the all method. """
    #     F_storage = FileStorage()
    #     object_1 = storage.all()
    #     self.assertEqual(type(object_1), dict)
    #     # self.assertEqual(type(F_storage.all()), dict)
    #     # self.assertTrue(hasattr(F_storage, 'all'), True)
    #     self.assertTrue(len(FileStorage.all.__doc__) > 0)
    #     self.assertIs(object_1, storage._FileStorage__objects)

    # def test_new(self):
    #     """ Test that checks the new method. """
    #     storage_2 = FileStorage()
    #     B_model = BaseModel()
    #     storage_2.new(B_model)
    #     self.assertTrue(storage_2.all())
    #     B_model.name = 'Da_Sa'
    #     self.assertEqual(B_model.name, 'Da_Sa')
    #     B_model.age = 89
    #     self.assertEqual(B_model.age, 89)
    #     self.assertTrue(hasattr(B_model, 'id'))
    #     self.assertEqual(type(B_model.id), str)
    #     self.assertTrue(hasattr(storage, 'new'), True)
    #     self.assertTrue(len(FileStorage.new.__doc__) > 0)
    #     self.assertEqual(type(B_model), models.base_model.BaseModel)
    #     with self.assertRaises(AttributeError):
    #         storage_2.new('string')
    #     with self.assertRaises(AttributeError):
    #         storage_2.new(float('nan'))
    #     with self.assertRaises(AttributeError):
    #         storage_2.new(float('inf'))

#    def test_save(self):
#        """ Test that checks the save method. """
#        self.F_storage.new(self.B_model)
#        self.F_storage.save()
#        self.assertTrue(os.path.isfile('file.json'))
#        self.assertTrue(hasattr(self.F_storage, 'save'), True)
#        self.assertEqual(os.path.isfile('file.json'), True)
#        self.assertGreater(self.B_model.updated_at, self.B_model.created_at)

#    def test_reload(self):
#        """ Test that checks the reload method. """
#        key = 'BaseModel' + '.' + self.B_model.id
#        self.F_storage.new(self.B_model)
#        self.F_storage.save()
#        self.F_storage.reload()
#        self.assertTrue(self.F_storage.all()[key])
#        self.assertTrue(hasattr(self.F_storage, 'reload'), True)

    # def test_FileStorage_empty(self):
    #     """ Test that checks the empty FileStorage. """
    #     self.assertIsNotNone(FileStorage.__doc__)
    #     self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == '__main__':
    unittest.main()
