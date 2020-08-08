#!/usr/bin/python3
"""A file that contains the class definition of a
State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class - the represention of table states in mysql database hbtn_0e_6_usa
        __tablename__ = name of the table
        id = states id
        name = name of the state
        """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
