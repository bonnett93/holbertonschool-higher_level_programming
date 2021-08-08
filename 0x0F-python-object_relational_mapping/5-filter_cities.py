#!/usr/bin/python3
"""Module: 5-filter_cities
    takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    # User credentials
    host_name = 'localhost'
    host_port = 3306
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL DB
    db = MySQLdb.connect(host_name,
                         user_name,
                         user_pass,
                         db_name,
                         port=host_port)

    # Select/create a cursor
    cursor = db.cursor()

    sql = """SELECT cities.name FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name = %s"""

    cursor.execute(sql, (state_name,))

    result = cursor.fetchall()

    cursor.close()
    db.close()

    if len(result) == 0:
        print("")

    for i in range(len(result)):
        if i < len(result) - 1:
            print(result[i][0], end=", ")
        else:
            print(result[i][0])
