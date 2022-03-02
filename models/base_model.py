#!/usr/bin/python3
"""
Module to write a class BaseModel.
"""


from uuid import uuid4
from datetime import datetime
from models import storage
date = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """ Initializes the data. """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        # Establecemos el valor del atributo especificado
                        # del objeto especificado.
                        setattr(self, key, datetime.strptime(value, date))
                    setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(kwargs)

    def __str__(self):
        """ Return string representation. """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """ Updates attribute updated_at with the current datetime. """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        new_dict = self.__dict__.copy()
        for key, value in new_dict.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = datetime.isoformat(value)
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
