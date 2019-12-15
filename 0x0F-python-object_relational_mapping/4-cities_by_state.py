#!/usr/bin/python3
import sys
import MySQLdb

'''
module for cities
'''
_SQL = """

SELECT
    cities.id, states.name, cities.name
FROM
    cities
        INNER JOIN
    states ON cities.state_id = states.id
    ORDER BY cities.id ASC

"""


def get_db_connexion(**kwargs):
    '''
    get database connexion
    '''
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", **kwargs)
    return conn


def make_query(conn):
    '''
    lists all cities from the database hbtn_0e_4_usa
    preventing sql injection
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
    make_query(get_db_connexion(
        user=user, passwd=passwd, db=db))
