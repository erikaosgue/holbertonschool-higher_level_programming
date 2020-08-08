#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv


def main():
    """ main function """
    if len(argv) == 5:
        my_user = argv[1]
        my_passw = argv[2]
        my_db = argv[3]
        states_name = argv[4]
        try:
            db = MySQLdb.connect(host="localhost", user=my_user,
                                 passwd=my_passw, db=my_db, port=3306)
        except:
            print("[Error]: one or more argms invalid")
            return 0
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM states WHERE states.name in (%s)
                       ORDER BY states.id""", (states_name,))
        cursor.fetchall()
        for row in cursor:
            print(row)
        db.close()


if __name__ == "__main__":
    main()
