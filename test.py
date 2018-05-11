import MySQLdb

try:
    conn = connect('localhost', 'root', 'root', 'test')
    cursor1 = conn.cursor()

    cursor1.execute('drop table if exists student')
    data = cursor1.fetchone()
    print data

    cursor1.close()
    conn.close()
except Exception, e:
    print e.message
