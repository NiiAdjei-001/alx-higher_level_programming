#!/usr/bin/python3
""" Model State Fetch All States Contain 'a'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


argv = sys.argv
if __name__ == "__main__":
    if argv.__len__() == 4:
        url = 'mysql://{}:{}@{}:{}/{}'.format(argv[1],
                                              argv[2],
                                              'localhost',
                                              '3306',
                                              argv[3])
        engine = create_engine(url)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        for record in session.query(State) \
                .filter(State.name.ilike('%a%')) \
                .order_by(State.id.asc()):
            print("{}: {}".format(record.id, record.name))
        session.close()
