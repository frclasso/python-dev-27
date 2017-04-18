#!/usr/bin/python

#conding:utf-8

import pgdb

con = pgdb.connect(database='music')

"""con = pgdb.connect(host='tao', database='music', user='pg', password='senha'
"""
cur = con.cursor()

sql = 'create table tracks '\
'(id serial primary key, '\
'track varchar (100),'\
'band varchar(100))'
cur.execute(sql)

sql = 'insert into tracks values (default, %s ,%s)'

#dados
recset = [('Kashimir', 'Led Zeppelin'),
          ('Starless','King Crimson')]

#insere os registros
for rec in recset:
	cur.execute(sql, rec)

con.commit()

#recupera registros
cur.execute('select * from tracks')

#recupera resultados
recset = cur.fetchall()
for rec in recset:
	print rec

con.close()