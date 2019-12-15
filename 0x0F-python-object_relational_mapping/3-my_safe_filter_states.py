#!/usr/bin/python3
import sys
import MySQLdb

'''
module for states
'''
_SQL = """ SELECT * FROM states
            WHERE  states.name LIKE %s
            ORDER BY states.id ASC"""


def get_db_connexion(**kwargs):
    '''
    get database connexion
    '''
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", **kwargs)
    return conn


def get_all_states(conn, state_name):
    '''
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument and preventing sql injection
    '''
    cur = conn.cursor()
    cur.execute(_SQL, (state_name, ))
    query_rows = cur.fetchall()
    for item in query_rows:
        if item[1] == state_name:
            print(item)
    cur.close()
    conn.close()


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    get_all_states(get_db_connexion(
        user=user, passwd=passwd, db=db), state_name)
