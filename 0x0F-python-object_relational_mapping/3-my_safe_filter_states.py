#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argumentBut this time, write one
that is safe from MySQL injections! """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 5:
        print("Error")
        exit(1)

    search = '{}'.format(argv[4])
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    # create cursor object
    cursor = db.cursor()
    # MySQL execution
    cursor.execute('SELECT id, name FROM states '
                   'WHERE name = %s '
                   'ORDER BY states.id ASC', (search,))
    for row in cursor.fetchall():
        print(row)
