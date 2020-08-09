#!/usr/bin/python3
""" A script that prints the first State
object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # connect into the Session class
    Session = sessionmaker(bind=engine)
    # to have a conversation with the data base
    # i have to instantiate a Session
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
