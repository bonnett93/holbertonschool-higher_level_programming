#!/usr/bin/python3
'''Module: 1-filter_states
    lists all states with a name starting with N
    from the database hbtn_0e_0_usa'''

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

    # Make a query
    sql = """SELECT * FROM states
            WHERE BINARY states.name Like 'N%'
            ORDER BY states.id
            """

    cursor.execute(sql)

    result = cursor.fetchall()

    cursor.close()
    db.close()

    for each in result:
        print(each)
