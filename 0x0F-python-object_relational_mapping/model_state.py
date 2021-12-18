#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance
Base = declarative_base():
"""


from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This class represents the table called states."""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False, )
