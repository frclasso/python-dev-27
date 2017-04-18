#!/usr/bin/python

#coding:utf-8
import MySQLdb

con = MySQLdb.connect(db='test', user='root', passwd='senha')
cur = con.cursor()

#executa comando sql showdatabases
cur.execute('showdatabases')

#recupera resultado
recordset = curt.fetchall()

#exibe resultado
for record in recordset:
	print record


con.close()