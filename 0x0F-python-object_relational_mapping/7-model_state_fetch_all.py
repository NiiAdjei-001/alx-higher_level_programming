#!/usr/bin/python3
""" Model State Fetch All Module
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State


argv = sys.argv
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
    
    records = session.query(State)
    for record in records:
        print("{}: {}".format(record.id, record.name))
    session.close()
