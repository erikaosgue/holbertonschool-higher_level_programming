#!/usr/bin/python3
"""A file that contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class - the represention of table City in mysql
       database hbtn_0e_14_usa

        __tablename__ = name of the table
        id = states id
        name = name of the state
        """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
