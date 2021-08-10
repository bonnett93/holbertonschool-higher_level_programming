#!/usr/bin/python3
"""Module: 11-model_state_insert
    adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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

    new_state = State(name='Louisiana')
    session.add(new_state)

    result = session.query(State).order_by(State.id.desc()).first()

    print(result.id)

    session.close()
