#!/usr/bin/python3
"""
Module to write a class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review that inherit from BaseModel. """
    place_id = ''  # Place.id
    user_id = ''  # User.id
    text = ''

    def __init__(self, *args, **kwargs):
        """ Initializes Review. """
        super().__init__(*args, **kwargs)
