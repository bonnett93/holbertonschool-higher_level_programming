#!/usr/bin/python3
"""Module: 8-model_state_fetch_first
    prints the first State object from the database hbtn_0e_6_usa"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    uname = sys.argv[1]
    upass = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    # dialect+driver://username:password@host:port/database
    engie = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.
                          format(uname, upass, port, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engie)
    session = Session()

    sql = session.query(State)
    result = sql.first()

    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")

    session.close()
