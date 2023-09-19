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
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')

    # Create a session using the sessionmaker method
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the tables specified in models
    Base.metadata.create_all(engine)

    # Query the db for what you want
    statesList = session.query(State).order_by(State.id).all()
    for state in statesList:
        print(f'{state.id}: {state.name}')

    # close the current session once all states are printed
    session.close()
