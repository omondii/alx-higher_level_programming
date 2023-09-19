#!/usr/bin/python3
"""
Imported modules
sys
Base, State from model_state
create_engine
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}, pool_pre_ping=True')

    # Create a session using the sessionmaker method
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    # Create the search Query
    state = sys.argv[4]
    newState = session.query(State).filter(State.name == state).order_by(State.id).first()

    # Print the queryresults
    if newState:
        print(f'{states.id}')
    else:
        print("Not found")
