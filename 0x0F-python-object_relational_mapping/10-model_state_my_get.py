#!/usr/bin/python3
'''
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    filter_state = session.query(State).filter(State.name == argv[4]).all()
    if not filter_state:
        print('Not found')
    for state in filter_state:
        print("{:d}".format(state.id))
    session.close()
