#!/usr/bin/python3
import sys
import MySQLdb

'''
module for cities
'''
_SQL = """

SELECT
    cities.name
FROM
    cities
        INNER JOIN
    states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC

"""


def get_db_connexion(**kwargs):
    '''
    get database connexion
    '''
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", **kwargs)
    return conn


def make_query(conn, state_name):
    '''
    lists all cities from the database hbtn_0e_4_usa
    All cities by state
    preventing sql injection
    '''
    cur = conn.cursor()
    cur.execute(_SQL, (state_name, ))
    query_rows = cur.fetchall()
    print(", ".join(item[0] for item in query_rows))
    cur.close()
    conn.close()


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    make_query(get_db_connexion(
        user=user, passwd=passwd, db=db), state_name)
