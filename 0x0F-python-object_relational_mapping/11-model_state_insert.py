#!/usr/bin/python3
"""This script adds the State object “Louisiana” to
the database hbtn_0e_6_usa"""

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

    new_state = State(name='Louisiana')
    session.add(new_state)
    query = session.query(State).filter_by(name='Louisiana').first()
    print(new_state.id)
    session.commit()
    session.close()
