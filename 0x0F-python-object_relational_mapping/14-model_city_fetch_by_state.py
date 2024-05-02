#!/usr/bin/python3
""" Model State - Delete States Contain 'a'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

        records = session.query(State.name, City.id, City.name) \
            .outerjoin(City).filter(State.id == City.state_id) \
            .order_by(City.id).all()
        for state, city_id, city_name in records:
            print("{}: ({}) {}".format(state, city_id, city_name))
        session.close()
