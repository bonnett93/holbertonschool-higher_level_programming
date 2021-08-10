#!/usr/bin/python3
"""Module: 14-model_city_fetch_by_state
    prints all City objects from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    uname = sys.argv[1]
    upass = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    port = 3306

    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.
                          format(uname, upass, host, port, db),
                          pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    sql = session.query(State.name, City.id, City.name).join(State)
    result = sql.order_by(City.id).all()

    for each in sql:
        print("{}: ({}) {}".format(each[0], each[1], each[2]))

