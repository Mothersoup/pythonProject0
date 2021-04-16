import mysql.connector
import pymysql


def update(a, b, c):
    db = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='kk95681932',
        database='con',
        charset='utf8'
    )
    cur = db.cursor()
    sql = """UPDATE xyz SET x='%s' WHERE id=1""" % a
    sql2 = """UPDATE xyz SET y='%s' WHERE id=1""" % b
    sql3 = """UPDATE xyz SET z='%s' WHERE id=1""" % c
    cur.execute(sql)
    cur.execute(sql2)
    cur.execute(sql3)
    db.commit()


update(4, 5, 5)
