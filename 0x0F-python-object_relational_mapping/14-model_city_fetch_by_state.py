#!/usr/bin/python3
'''
print all relationship cities, states
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    for city, state in cities:
        print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))

    session.close()
