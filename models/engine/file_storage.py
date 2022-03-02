#!/usr/bin/python3
"""
Module to write a class FileStorage
"""
import json
import os.path
import uuid
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    # String - path to the JSON file (ex: file.json)
    __file_path = 'file.json'
    # Dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + str(uuid.uuid4())  # obj.id, BaseModel.id
        # In dictionaries, if the key does not exist, it creates it
        # and if it does exist, it replaces it.
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ Seserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    self.__objects = json.loads(file)
            except Exception:
                pass
