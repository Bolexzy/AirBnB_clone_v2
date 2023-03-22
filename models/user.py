#!/usr/bin/python3
"""
    Defines a User class that inherits from BaseModel.
"""
from models.base_model import (BaseModel, Base)
from os import getenv
from sqlalchemy import (Column, String)


class User(BaseModel, Base):
    """Represents a class User.
    Inherits from BaseModel and SQLAlchemy Base
    and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
