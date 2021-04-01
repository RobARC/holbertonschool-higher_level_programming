#!/usr/bin/python3
""" script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # conector to data base with parameters recivied from console
    db = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(mysql_username,
          mysql_password, database_name))

    # engine conection
    engine = create_engine(db, pool_pre_ping=True)

    # Creates all classes currently active.
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    # create session's cursor.
    session = Session()

    # Create Query.
    queryState = session.query(State).order_by(State.id).all()

    # Print on a specific format.
    for state in queryState:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    
    # Close session.

    session.close()


if __name__ == "__main__":
    main()
