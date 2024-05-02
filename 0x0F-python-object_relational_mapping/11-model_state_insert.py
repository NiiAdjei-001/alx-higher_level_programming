#!/usr/bin/python3
""" Model State - Insert States With name = 'Louisiana'
"""
from sqlalchemy import create_engine
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

        new_state = State(name='Louisiana')
        session.add(new_state)
        id, = session.query(State.id) \
            .where(State.name == new_state.name).first()
        print(id)
        session.commit()
        session.close()
