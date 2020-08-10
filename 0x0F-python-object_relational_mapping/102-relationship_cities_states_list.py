#!/usr/bin/python3
""" A script that lists all City objects from the database hbtn_0e_101_usa"""

from sys import argv
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # engine = create_engine(
    # 'mysql+mysqldb://username:password@localhost/database')
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    # connect into the Session class
    Session = sessionmaker(bind=engine)
    # to have a conversation with the data base
    # i have to instantiate a Session
    session = Session()

    # city.state.name is due to the relationship that State class made
    # this means that the City class will be having a "new" attribute
    # call "state", this is for the backref
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
