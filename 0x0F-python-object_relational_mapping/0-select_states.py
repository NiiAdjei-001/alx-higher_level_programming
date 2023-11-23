#!/usr/bin/python3
"""
Select States Module
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
    query = "SELECT id, name FROM states;"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
