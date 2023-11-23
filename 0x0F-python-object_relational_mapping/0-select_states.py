#!/usr/bin/python3
"""
Select States Module
"""
import MySQLdb


DB_DETAIL = {
    'host': "localhost",
    'port': 3306,
    'user': "beta_usr",
    'passwd': "beta_pwd",
    'db': "hbtn_0e_0_usa"
}
ALX_DB_DETAIL = {
    'host': "localhost",
    'port': 3306,
    'user': "root",
    'passwd': "root",
    'db': "hbtn_0e_0_usa"
}
db = MySQLdb.connect(**ALX_DB_DETAIL)
cursor = db.cursor()
query = "SELECT id, name FROM states;"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)
