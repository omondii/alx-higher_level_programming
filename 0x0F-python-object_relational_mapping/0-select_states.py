#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
Your script should connect to a MySQL server running on localhost at port 3306
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # set up the db connection with all required params
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    # create a cursor object
    cursor = db.cursor()

    cursor.execute('SELECT id, name FROM states ORDER BY states.id ASC')

    for row in cursor.fetchall():
        print(row)
