#!/usr/bin/python3
""" A script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    # connect into the Session class
    Session = sessionmaker(bind=engine)
    # to have a conversation with the data base
    # i have to instantiate a Session
    session = Session()

    find_state = False
    for state in session.query(State):
        if state.name == argv[4]:
            print("{}".format(state.id))
            find_state = True
            break

    if find_state is False:
        print("Not found")
