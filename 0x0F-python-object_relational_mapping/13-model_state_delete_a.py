#!/usr/bin/python3
# list all cities from database
from model_state import Base, State
from sqlalchemy import create_engine, update, delete
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
    objs = session.query(State).filter(State.name.like('%a%'))
    for obj in objs:
        session.delete(obj)
    session.commit()
    session.close()
