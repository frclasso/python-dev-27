#!/usr/bim/python

#coding: utf-8

import psycopg2

con = psycopg2.connect(database='music')
cur = con.cursor()
sql  = 'insert into tracks values(default, %s, %s)'
recset = [('Siberian Kathru', 'Yes'),
           ("Supper's Ready", 'Genesis')]

for rec in recset:
	cur.execute(sql, rec)
con.commit()

cur.execut('select * from tracks')
recset = cur.fetchall()
for rec in recset:
	print rec

con.close()