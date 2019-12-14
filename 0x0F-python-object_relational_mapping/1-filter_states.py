#!/usr/bin/python3
import sys
import MySQLdb

'''
module for states
'''
_SQL = """ SELECT * FROM states
            WHERE  states.name LIKE 'N%'
            ORDER BY states.id ASC"""


def get_db_connexion(**kwargs):
    '''
    get database connexion
    '''
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", **kwargs)
    return conn


def get_all_states(conn):
    '''
    lists all states with a name starting with N
    print all states order by id
    '''
    cur = conn.cursor()
    cur.execute(_SQL)
    query_rows = cur.fetchall()
    for item in query_rows:
        print(item)
    cur.close()
    conn.close()


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    get_all_states(get_db_connexion(user=user, passwd=passwd, db=db))
