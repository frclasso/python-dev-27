#!/usr/bin/python

#coding: utf-8

import kinterbasdb

con = kinterbasdb.connect(dsn='localhost:temp/cds.fdb', user='sysdba', password='senha')

cur = con.cursor()

sql = "create table cds("\
"nome varchar(20),"\
"artista varchar(20)"\
"ano integer, "\
"faixas integer,"\
"primary key(nome, artista, ano));"

#cria uma tabela
cur.execute(sql)

con.commit()

dados = [
   ('IV', 'Led Zeppelin', 1971, 8),
   ('Zenyatta Mondatta', 'The Police', 1980, 11),
   ('OK Computer', 'Radio Head', 1997, 12),
   ('In Absentia', 'Porcupine Tree', 2002, 12),
]

#insere resultados e faz interpolacao
insert = "insert into cds"\
"(nome, artista, ano, faixaas) values (?,?,?,?)" 
cur.executemany(insert, dados)
con.commit()

#consulta registros
cur.execute("select * from cds order by ano")

#recupera dados
for reg in cur.fetchall():
    print '-'.join(str(i) for i in reg)