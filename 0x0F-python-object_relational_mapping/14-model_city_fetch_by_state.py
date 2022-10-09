#!/usr/bin/python3

"""
This script lists all state objects from database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sys import argv

from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    db_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    if len(argv) >= 4:
        engine = create_engine(db_string.format(
            argv[1],
            argv[2],
            argv[3]))
        State.cities = relationship('City', back_populates='state')
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = session.query(City).order_by(City.id.asc()).all()

        for row in result:
            print('{}: ({}) {}'.format(row.state.name, row.id, row.name))

        session.close()
