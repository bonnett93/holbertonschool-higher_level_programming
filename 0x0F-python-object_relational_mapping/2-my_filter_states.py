#!/usr/bin/python3
"""Module: 2-my_filter_states.py
    takes in an argument
    and displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument."""

if __name__ == '__main__':
    import sys
    import MySQLdb

    # User credentials
    host_name = 'localhost'
    host_port = 3306
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    # Connect to MySQL DB
    db = MySQLdb.connect(host_name,
                         user_name,
                         user_pass,
                         db_name,
                         port=host_port)

    # Select/create a cursor
    cursor = db.cursor()

    # Make a query
    sql = """SELECT * FROM states
            WHERE states.name='{}'
            ORDER BY states.id""".format(name)

    cursor.execute(sql)

    result = cursor.fetchall()

    cursor.close()
    db.close()

    for each in result:
        print(each)
