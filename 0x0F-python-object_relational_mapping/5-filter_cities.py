#!/usr/bin/python3
""" a script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv


def main():
    """ main function """
    if len(argv) == 5:
        my_user = argv[1]
        my_passw = argv[2]
        my_db = argv[3]
        state_name = argv[4]
        try:
            db = MySQLdb.connect(host="localhost", user=my_user,
                                 passwd=my_passw, db=my_db, port=3306)
        except:
            print("[Error]: one or more argms invalid")
            return 0

        cursor = db.cursor()
        cursor.execute("""SELECT cities.name
                          FROM cities
                          JOIN states ON cities.state_id = states.id
                          WHERE states.name = (%s)
                          ORDER BY states.id""", (state_name,))
        cursor.fetchall()
        my_list = ", ".join(row[0] for row in cursor)
        print(my_list)
        db.close()


if __name__ == "__main__":
    main()
