#!/usr/bin/python3

"""
This script lists all state objects from database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    data = session.query(State).filter(
        State.name.like("%a%")).delete(
            synchronize_session='fetch')
    session.commit()

    session.close()
