#!/usr/bin/python3
""" Model State Fetch All Module
"""
import MySQLdb
import sys
from model_state import Base, State


argv = sys.argv
if argv.__len__() == 4:
    ALX_DB_DETAIL = {
        'host': "localhost",
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3]
    }
    db = MySQLdb.connect(**ALX_DB_DETAIL)
    cursor = db.cursor()
    query = """SELECT id, name
            FROM states
            ORDER BY states.id ASC;"""
    cursor.execute(query)
    records = cursor.fetchall()
    my_list = [x[0] for x in records]
    for record in records:
        print("{}: {}".format(record[0], record[1]))
    cursor.close()
    db.close()
