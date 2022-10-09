#!/usr/bin/python3

"""
This script lists all state objects from database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

if __name__ == '__main__':
    if len(argv) >= 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3]))
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = session.query(State).order_by(State.id.asc()).filter(
            State.name.like('%a%')
        )
        for first_state in result:
            print("{}: {}".format(first_state.id, first_state.name))
        

        session.close()
