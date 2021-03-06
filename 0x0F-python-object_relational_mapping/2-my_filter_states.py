#!/usr/bin/python3
"""
This scrips allows to connect with database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Connecting to MySQL database, getting a cursor and executing queries."""

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT id, name FROM states WHERE name
    LIKE BINARY '{:s}' ORDER BY id ASC""".format(argv[4]))
    query_states = cursor.fetchall()
    for state in query_states:
        print(state)
    cursor.close()
    db.close()
