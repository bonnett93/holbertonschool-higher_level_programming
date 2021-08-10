#!/usr/bin/python3
"""Module: 10-model_state_my_get
    prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine, func
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    uname = sys.argv[1]
    upass = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]
    port = 3306

    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.
                           format(uname, upass, port, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    sql = session.query(State).filter(State.name == func.binary(name))
    result = sql.all()

    for each in result:
        print(each.id)

    if (not result):
        print('Not found')

    session.close()
