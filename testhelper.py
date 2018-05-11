# coding:utf8
from mysqlhelper import mysqlHelper

# name=raw_input('请输入学生姓名:')
# id=int(raw_input('请输入学生编号:'))

sql = 'drop table if exists student'
params = []

sqlhelper = mysqlHelper('localhost', 3306, 'test', 'root', 'root')
sqlhelper.cud(sql, params)
