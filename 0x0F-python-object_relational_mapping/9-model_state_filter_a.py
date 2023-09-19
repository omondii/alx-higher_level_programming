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

    criteria = State.name.like('%a%')

    # Query the db for all cities with a
    stateA = session.query(State).filter(criteria).order_by(State.id).all()

    # Print the records that match the criteria
    for state in stateA:
        print(f'{state.id}: {state.name}')

    # close the session when done
    session.close()
