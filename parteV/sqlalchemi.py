#!/usr/bin/python

# -*-coding: latin1 -*-
#testando o Alchemy

from sqlalchemy import *

db = create_engine('sqlite:///progs.bd')
metadata = MetaData(db)

#echoa o que o SQLALCHEMY esta fazendo
metadata.bind.echo=True

#Tabela prog
prog_table = Table('progs', metadata, 
	          Column('prog_id', Integer,primary_key=True),
	          Column('name', String(80)))


#cria tabela
prog_table.create()

#carrega a definicao da tabela
prog_table = Table('progs', metadata, autoload=True)

#insere dados
i = prog_table.insert()
i.execute({'name':'Yes'}, {'name': 'Genesis'}, {'name': 'Pink Floyd'}, {'name': 'King Crimson'})

#seleciona
s = prog_table.select()
r = s.execute()

for row in r.fetchall():
	print row