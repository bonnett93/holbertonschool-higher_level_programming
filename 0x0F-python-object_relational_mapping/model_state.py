#!/usr/bin/python3
"""Module: model_state
    contains the class definition of a State
    and an instance Base = declarative_base()"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


uname = 'root'
upass = '1q2w3e4r5t'
port = 3306
db = 'hbtn_0e_6_usa'

# dialect+driver://username:password@host:port/database
engie = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(uname,
                                                                     upass,
                                                                     port,
                                                                     db))

Base = declarative_base()


class State(Base):
    """Class that define the table 'states' """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
