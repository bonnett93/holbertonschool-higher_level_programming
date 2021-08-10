#!/usr/bin/python3
"""Module: model_city
    contains the class definition of a City
    and an instance Base = declarative_base()"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """Class that define the table 'cities' """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
