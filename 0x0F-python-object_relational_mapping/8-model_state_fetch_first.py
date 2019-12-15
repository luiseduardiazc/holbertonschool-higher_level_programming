#!/usr/bin/python3
'''
script that lists all State objects from the database hbtn_0e_6_usa
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                       argv[2],
                                                                       argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_filter = session.query(State).order_by(State.id).first()
    if not state_filter:
        print('Nothing')
    else:
        print("{:d}: {:s}".format(state_filter.id, state_filter.name))
    session.close()
