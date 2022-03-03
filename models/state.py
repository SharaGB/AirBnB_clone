#!/usr/bin/python3
"""
Module to write a class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class State that inherit from BaseModel. """
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initializes State. """
        super().__init__(*args, **kwargs)
