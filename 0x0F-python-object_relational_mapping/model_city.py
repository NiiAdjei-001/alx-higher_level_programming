#!/usr/bin/python3
"""State Model ORM Module
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from model_state import Base


class City(Base):
    """State Class Model"""
    __tablename__ = 'cities'

    id = Column(Integer, Sequence('state_id_seq'), primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<City (id={self.id}, name={self.name}, state_id={self.state_id})>"
