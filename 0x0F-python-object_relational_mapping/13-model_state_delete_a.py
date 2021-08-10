#!/usr/bin/python3
"""Module: 13-model_state_delete
    deletes all State objects with a name containing the letter 'a'
    from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    uname = sys.argv[1]
    upass = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.
                           format(uname, upass, port, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    sql = session.query(State).filter(State.name.like("%a%"))
    print(sql)
    result = sql.all()
    for each in result:
        session.delete(each)

    session.commit()

    session.close()
