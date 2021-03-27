#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


def main():

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect("localhost",
                         mysql_username,
                         mysql_password,
                         database_name,
                         3306)

    cursor = db.cursor()
    cursor.execute(
        "select cities.id, cities.name, states.name\
         from cities inner join states on cities.state_id = states.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
