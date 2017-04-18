#!/usr/bin/python 

# -*- coding: latin1 -*-
import cherrypy
import cherrytemplate
import sqlalchemy as sql


db = sql.create_engine('sqlite:///zoo.db')

metadata = sql.MetaData(db)

try:
	zoo = sql.Table('zoo', metadata, autoload=True)
except:
	zoo = sql.Table('zoo', metada,
		   sql.Column('id', sql.Integer, primarykey=True),
		   sql.Column('nome', sql.String(100),
		   	unique=True, nullable=False),
		   sql.Column('quantidade', sql.Integer, default=1),
		   sql.Column('obs', sql.String(200), default='')
		   )

zoo.create()
#nomes das colunas
colunas = [col for col in zoo.columns.keys()]
colunas.remove('id')

class Root(object):
	@cherrypy.expose
	def index(self, **args):
		#lista os registros
		msg = ''
		op = args.get('op')
		ident =int(args.get('ident', 0))
		novo = {}
        for coluna in colunas:
            novo[coluna] = args.get(coluna)

        if op == 'rem':
        	rem  = zoo.delete(zoo.c.id==ident)
        	rem.execute()
        	msg = 'registro removido'

        elif op =='add':
        	novo = {}

        	for coluna in colunas:
        		novo[coluna] = args[coluna]

        	try:
        		#insere dados
        		ins = zoo.insert()
        		ins.execute(novo)
        		msg = 'registr adicionado'

        	except sql.exceptions.IntegrityError:
        		msg = 'registr existe'

        elif op == 'mod':
        	novo = {}
        	for coluna in colunas:
        		novo[coluna] =  args[coluna]
        	try:
        		#modifica dados
        		mod = zoo.update(zoo.c.id==ident)
        		mod.execute(novo)
        		msg='registro modificado'
        	except sql.exceptions.IntegrityError:
        		msg = 'registro exite'
		sel = zoo.select(order_by=zoo.c.nome)
		rec = sel.execute()
		return cherrytemplate.renderTemplate(file='index.html', outputEncoding='utf-8')

	@cherrypy.expose
	def add(self):
	#cadastra novos registros
	    return cherrytemplate.renderTemplate(file='add.html', outputEncoding='utf-8')

	@cherrypy.expose	
	def rem(self, ident):
    	#confirma remocao dos dados
		sel = zoo.select(zoo.c.id==ident)
		rec = sel.execute()
		res = rec.fetchone()
		return cherrytemplate.renderTemplate(file='rem.html', outputEncoding='utf-8')

	@cherrypy.expose
	def mod(self, ident):
        #modifca os registros
		sel = zoo.select(zoo.c.id==ident)
		rec = sel.execute()
		res = rec.fetchone()
		return cherrytemplate.renderTemplate(file='mod.html', outputEncoding='utf-8')


cherrypy.quickstart(Root())        