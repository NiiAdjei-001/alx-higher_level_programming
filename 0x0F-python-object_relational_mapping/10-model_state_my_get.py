#!/usr/bin/python3
""" Model State Fetch All States Contain 'a'
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


argv = sys.argv
if __name__ == "__main__":
    if argv.__len__() >= 5:
        url = 'mysql://{}:{}@{}:{}/{}'.format(argv[1],
                                              argv[2],
                                              'localhost',
                                              '3306',
                                              argv[3])
        engine = create_engine(url)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        stmt = select(State.id).where(State.name == argv[4])
        record = session.execute(stmt).first()
        if record:
            print("{}".format(record.id))
        else:
            print("Not found")
        session.close()
