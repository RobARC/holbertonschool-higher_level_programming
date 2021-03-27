#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


def main():

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_search = sys.argv[4]

    db = MySQLdb.connect("localhost",
                         mysql_username,
                         mysql_password,
                         database_name,
                         3306)

    cursor = db.cursor()
    cursor.execute(
        ("SELECT cities.name FROM cities\
        LEFT JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s ORDER BY cities.id ASC"), (state_search, ))

    print(", ".join(row[0] for row in cursor.fetchall()))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
