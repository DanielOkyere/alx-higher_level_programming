#!/usr/bin/python3

"""
    This is the first model created defining state and
    base instance.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base


class City(Base):
    """
        Representation of a row in cities table
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False
                      )
    state = relationship('State', back_populates='cities')
