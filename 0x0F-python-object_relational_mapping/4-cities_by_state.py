#!/usr/bin/python3
""" A a script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv


def main():
    """ main function """
    if len(argv) == 4:
        my_user = argv[1]
        my_passw = argv[2]
        my_db = argv[3]
        try:
            db = MySQLdb.connect(host="localhost",
                                 user=my_user,
                                 passwd=my_passw,
                                 db=my_db,
                                 port=3306)
        except:
            return 0

        cursor = db.cursor()
        cursor.execute("""SELECT cities.id, cities.name, states.name
                          FROM cities
                          JOIN states ON cities.state_id = states.id
                          ORDER BY states.id""")
        cursor.fetchall()
        for row in cursor:
            print(row)
        db.close()


if __name__ == "__main__":
    main()
