#!/usr/bin/python3
""" script that creates the State “California” with the City “San Francisco” 
    from the database hbtn_0e_100_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import relationship, sessionmaker


def create_state_and_city():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_username = sys.argv[3]

    # conector to data base with parameters recivied from console
    db = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(mysql_username, 
          mysql_password, database_name))

    # engine conection 
    engine = create_engine(db, pool_pre_ping=True)

    # Creates all classes currently active.
    Base.metada.create_all(engine)

    Session = sessionmaker(bind=engine)
    
    #create session's cursor.
    session = Session()

    newState = State(name="California", cities=[City(name="San Francisco")])

    #Add the new state.
    session.add(newState)

    #Commit the change.
    session.commit()

    #Close session.

    session.close()


