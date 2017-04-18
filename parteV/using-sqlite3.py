#!/usr/bin/python

#coding:utf-8

import sqlite3

con = sqlite3.connect('emails.db')
cur = con.cursor()

#cria uma tabela
sql = 'create table emails '\
      '(id integer primary key, '\
      'nome varchar (100), '\
      'email varchar(100))'

cur.execute(sql)

#inserindo registros
sql = 'insert into emails values (null,?,?)'

#dados
recset = [('jane doe', 'jane@nowhere.org'), ('rock', 'rock@hardplace.com')]

#insere registros
for rec in recset:
	cur.execute(sql, rec)

#confirma transacao
con.commit()

#seleciona todos os registros
cur.execute('select * from emails')

#recupera resultados
recset = cur.fetchall()

#exibe
for rec in recset:
	print '%d: %s(%s)' % rec

con.close()
