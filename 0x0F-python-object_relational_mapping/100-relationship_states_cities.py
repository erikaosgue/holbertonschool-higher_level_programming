#!/usr/bin/python3
"""A script that creates the State “California”
 with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    # engine = create_engine(
    # 'mysql+mysqldb://username:password@localhost/database')
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # connect into the Session class
    Session = sessionmaker(bind=engine)
    # to have a conversation with the data base
    # i have to instantiate a Session
    session = Session()

    new_state_with_city = City(name="San Francisco")
    new_state_with_city.state = State(name="California")
    session.add(new_state_with_city)
    session.commit()
