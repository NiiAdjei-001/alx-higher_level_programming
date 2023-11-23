#!/usr/bin/python3
"""State Model ORM Module
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Sequence


Base = declarative_base()


class State(Base):
    """State Class Model"""
    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'), primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<State (id={self.id}, name={self.name})>"
