#!/usr/bin/python3

"""
This script lists all state objects from database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    db_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_string.format(
        argv[1],
        argv[2],
        argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    cities = session.query(City).join(State).order_by(City.id.asc())
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
