#!/usr/bin/python3

"""
    This Script lists all states from the database `hbtn_0e_4_usa`
    It takes username, password, database name
    Makes use of MySQLdb.
    Connects to MySQL server on localhost 3306
    Result must be sorted in ascending order by `states.id`
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    args = argv
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM states s
                JOIN cities c
                ON s.id = c.state_id
                ORDER BY c.id ASC;
                """)
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
