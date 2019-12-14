#!/usr/bin/python3
# list all cities from database
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in query:
        print("{}: {}".format(state.id, state.name))
    session.close()
