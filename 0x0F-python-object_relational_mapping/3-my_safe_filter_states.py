#!/usr/bin/python3
"""
My Safe Filter States Module
"""
import MySQLdb
import sys


argv = sys.argv
if argv.__len__() == 5:
    ALX_DB_DETAIL = {
        'host': "localhost",
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3]
    }
    search_n = argv[4]
    db = MySQLdb.connect(**ALX_DB_DETAIL)
    cursor = db.cursor()
    query = f"""SELECT id, name
            FROM states
            WHERE name = %s
            ORDER BY id ASC;"""
    cursor.execute(query, (search_n,))
    records = cursor.fetchall()
    for record in records:
        print(record)
    cursor.close()
    db.close()
