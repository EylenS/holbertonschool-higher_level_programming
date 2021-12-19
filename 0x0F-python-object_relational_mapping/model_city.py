#!/usr/bin/python3
"""
This module contains the class definition of a City
"""

from sqlalchemy.sql.expression import null
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """This class represents the table called cities"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey=('states.id'))
