#!/usr/bin/python3
"""
Module to write a class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity that inherit from BaseModel. """
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initializes Amenity. """
        super().__init__(*args, **kwargs)
