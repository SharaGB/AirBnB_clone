#!/usr/bin/python3
"""Module to write a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """create a User that inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the data."""
        super().__init__(*args, **kwargs)
