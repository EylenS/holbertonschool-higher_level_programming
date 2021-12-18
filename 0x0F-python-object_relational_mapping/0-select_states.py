#!/usr/bin/python3
"""This scrips allows to connect with database hbtn_0e_0_usa.
Should take 3 arguments:
n: user name
p: password
d: database name (no argument validation needed)"""

import MySQLdb
import sys


n = sys.argv[1]
p = sys.argv[2]
d = 'hbtn_0e_0_usa'


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=n, passwd=p, db=d)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_states = cursor.fetchall()
    for state in query_states:
        print(state)
    cursor.close()
    db.close()
