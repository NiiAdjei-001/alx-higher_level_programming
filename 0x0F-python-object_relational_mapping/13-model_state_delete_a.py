#!/usr/bin/python3
""" Model State - Delete States Contain 'a'
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


argv = sys.argv
if __name__ == "__main__":
    if argv.__len__() >= 4:
        url = 'mysql://{}:{}@{}:{}/{}'.format(argv[1],
                                              argv[2],
                                              'localhost',
                                              '3306',
                                              argv[3])
        engine = create_engine(url)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        states = session.query(State) \
            .filter(State.name.ilike('%a%')).all()
        for state in states:
            session.delete(states)
        session.commit()
        session.close()
