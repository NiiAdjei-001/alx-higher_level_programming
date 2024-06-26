#!/usr/bin/python3
""" Model State - Get States id from parsed parameter
"""
from sqlalchemy import create_engine
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

        record = session.query(State).where(State.name == argv[4]).first()
        if record:
            print("{}".format(record.id))
        else:
            print("Not found")
        session.close()
