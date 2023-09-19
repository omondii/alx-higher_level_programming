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

    # Query the db for first item only. Use the first() method
    firstState = session.query(State).first()

    # Print the query results
    if firstState:
        print(f'{firstState.id}: {firstState.name}')
    else:
        print("\n")
