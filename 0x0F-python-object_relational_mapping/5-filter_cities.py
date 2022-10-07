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
    cur.execute("""SELECT c.name FROM states s
                JOIN cities c
                ON s.id = c.state_id
                WHERE s.name = %(state)s
                ORDER BY c.id ASC;
                """, {'state': argv[4]})
    states = cur.fetchall()
    slenth = len(states)
    if slenth == 0:
        print('')
    for i in range(slenth):
        if i < slenth - 1:
            print(states[i][0], end=', ')
        else:
            print(states[i][0])

    cur.close()
    db.close()
