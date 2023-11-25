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
    query = """SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC;"""
    cursor.execute(query, (search_n,))
    records = cursor.fetchall()
    my_list = [ x[0] for x in records]
    print(", ".join(my_list))
    """ record_count = cursor.rowcount
    for i in range(0, record_count):
        if i == record_count-1:
            print(cursor.fetchone()[0])
        else:
            print(cursor.fetchone()[0], end=', ')"""
    cursor.close()
    db.close()
