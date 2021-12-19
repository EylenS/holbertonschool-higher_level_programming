#!/usr/bin/python3
"""This script deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""

import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """to be accessed directly for MetaData-specific operations."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))
    # a: State objects with a name containing the letter a.
    for a in query:
        session.delete(a)
    session.commit()
    session.close()
