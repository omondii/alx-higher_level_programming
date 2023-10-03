#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa: """
import MySQLdb
from sys  import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    # create cursor object
    cursor = db.cursor()

    # MySQL executi
    cursor.execute('SELECT id, name FROM states '
                   'ORDER BY states.id ASC')
    for row in cursor.fetchall():
        print(row)
