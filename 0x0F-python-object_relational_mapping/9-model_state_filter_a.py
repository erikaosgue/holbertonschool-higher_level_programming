#!/usr/bin/python3
""" A  script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
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

    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
