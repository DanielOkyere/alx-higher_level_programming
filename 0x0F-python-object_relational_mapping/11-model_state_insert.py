#!/usr/bin/python3

"""
This script lists all state objects from database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

if __name__ == '__main__':
    db_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_string.format(
        argv[1],
        argv[2],
        argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
