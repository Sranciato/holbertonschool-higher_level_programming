#!/usr/bin/python3
# Lists all states with a name starting with n
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
    c.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
    record = c.fetchall()
    for row in record:
        if row[1][:1] == "N":
            print("({}, \'{}\')".format(row[0], row[1]))
    c.close()
    db.close()
