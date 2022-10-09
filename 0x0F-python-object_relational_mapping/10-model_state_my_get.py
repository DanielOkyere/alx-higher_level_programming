#!/usr/bin/python3

"""
This script lists all state objects from database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

if __name__ == '__main__':
    if len(argv) >= 5:
        engine = create_engine("""mysql+mysqldb://
                               {}:{}@localhost:3306/{}""".format(
            argv[1],
            argv[2],
            argv[3]))
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        chk = map(lambda x: x.isalpha() or (x in (' ', '%', '_')),
                  argv[4])
        if not all(chk):
            argv[4] = ''
        result = session.query(State).filter(State.name == argv[4]).first()
        if result is not None:
            print("{}".format(result.id))
        else:
            print('Not found')

        session.close()
