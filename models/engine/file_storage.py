#!/usr/bin/python3
"""
Module to write a class FileStorage
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

new_classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'Amenity': Amenity,
    'Place': Place,
    'City': City,
    'Review': Review
}


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    # String - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # Dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # In dictionaries, if the key does not exist, it creates it
        # and if it does exist, it replaces it.
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                new_dict = json.loads(file.read())
            for key, value in new_dict.items():
                object = value['__class__']
                objects = object + '(**value)'
                self.__objects[key] = eval(objects)
