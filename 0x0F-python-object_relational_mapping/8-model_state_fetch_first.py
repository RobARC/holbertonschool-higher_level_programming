#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """


import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(mysql_username,
          mysql_password, database_name))

    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')

    session.close()


if __name__ == "__main__":
    main()
