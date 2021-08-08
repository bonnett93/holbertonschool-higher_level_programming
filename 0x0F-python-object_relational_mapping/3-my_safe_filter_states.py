#!/usr/bin/python3
"""Module: 3-my_safe_filter_states.py
    Similar to module 2... but with safe filter to prevent SQL injections"""

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
            WHERE states.name=%s"""

    cursor.execute(sql, (name, ))

    result = cursor.fetchall()

    cursor.close()
    db.close()

    for each in result:
        print(each)
