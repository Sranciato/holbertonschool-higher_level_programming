#!/usr/bin/python3
# takes name of state as argument and lists cities
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
        WHERE states.name=%s
        ORDER BY 'cities.id' ASC;""", (sys.argv[4], )
    )
    record = c.fetchall()
    i = len(record)
    end = 1
    for row in record:
        if end < i:
            print("{}, ".format(row[1]), end="")
        else:
            print("{}".format(row[1]))
        end += 1
    c.close()
    db.close()
