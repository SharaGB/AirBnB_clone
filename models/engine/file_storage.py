#!/usr/bin/python3
"""
Module to write a class FileStorage
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        temp_dict = {key: obj}
        self.__objects.update(temp_dict)

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update({key: value.to_dict()})
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """
        if os.path.exists(self.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    diction = json.loads(file.read())
                    for key, value in diction.items():
                        temp = self.classes[value["__class__"]](**value)
                        FileStorage.__objects[key] = temp
            except Exception:
                pass
