#!/usr/bin/python3
"""
My Safe Filter States Module
"""
import MySQLdb
import sys


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
    query = """SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;"""
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    cursor.close()
    db.close()
