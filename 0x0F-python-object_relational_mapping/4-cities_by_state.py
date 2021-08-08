#!/usr/bin/python3
"""Module: 4-cities_by_state
    lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    # User credentials
    host_name = 'localhost'
    host_port = 3306
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL DB
    db = MySQLdb.connect(host_name,
                         user_name,
                         user_pass,
                         db_name,
                         port=host_port)

    # Select/create a cursor
    cursor = db.cursor()

    sql = """SELECT cities.id, cities.name, states.name from cities
             JOIN states ON cities.state_id = states.id
             ORDER BY cities.id;"""

    cursor.execute(sql)

    result = cursor.fetchall()

    cursor.close()
    db.close()

    for each in result:
        print(each)
