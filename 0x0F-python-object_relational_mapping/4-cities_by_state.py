#!/usr/bin/python3
# list all cities
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    c = db.cursor()
    c.execute(
        """SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY 'cities.id' ASC;"""
    )
    record = c.fetchall()
    for row in record:
        print("({}, \'{}\', \'{}\')".format(row[0], row[1], row[2]))
    c.close()
    db.close()
