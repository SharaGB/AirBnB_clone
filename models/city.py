#!/usr/bin/python3
"""
Module to write a class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherit from BaseModel. """
    state_id = ''  # State.id
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initializes City. """
        super().__init__(*args, **kwargs)
