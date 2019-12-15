#!/usr/bin/python3
'''
script that changes the name of a State object from the database hbtn_0e_6_usa
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    states_to_delete = session.query(State).filter(State.name.like('%a%'))
    [session.delete(state) for state in states_to_delete]
    session.commit()
    session.close()
