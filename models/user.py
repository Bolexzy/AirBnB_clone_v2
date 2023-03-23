#!/usr/bin/python3
"""
    Defines a User class that inherits from BaseModel.
"""
from models.base_model import (BaseModel, Base)
from os import getenv
from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship


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
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship('Place', backref='user', cascade='all, delete')
        reviews = relationship('Review', backref='user', cascade='all, delete')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
