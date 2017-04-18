#!/usr/bin/python

#-*-coding: utf-8 -*-

class Singleton(type):
	#Metaclass Singleton
	def __init__(cls, name, base, dic):
		type.__init__(cls, name, base, dic)

		def __copy__(self):
			return self

		#Retorna o proprio objeto na copia recursiva
		def __deepcopy__(self, memo=None):
			return self

		cls.__copy__ = __copy__
		cls.__deepcopy__ = __deepcopy__

	def __call__(cls, *args, **kwargs):
	    #Chamada que cria novos objetos
	    try:
	        return cls._instance
	        #se a instancia nao existir
	    except AttributeError:
	        #Afuncao super() pesquisa no MRO a partir do Singleton
	        cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
	        return cls.__instance

import MySQLdb

class Con(object):
	#Classe de conexao unica
	#Define a metaclasse desta classe
	__metaclass_ = Singleton
	def __init__(self):
		#Cria um conexao com o cursor
		con = MySQLdb.connect(user=root)
		self.db = con.cursor()
		#sempre sera usado o mesmo objeto de cursor

class Log(object):
	"""Classe de Log"""
	#Define a metaclasse desta classe
	__metaclass_ = Singleton
	def __init__(self):
		#Abre arquivo de log para escrita
		self.log = ('msg.log', 'w')

	def write(self, msg):
	    print msg
	    #Acrescenta uma mensagem no arquivo
	    self.log.write(str(msg)+'\n')

#Conexao1
con1 = Con()
Log().write('con1 id= %d' %id(con1))
con1.db.execute('show processlist')
Log().write(con1.db.fetchall())

#Conexao2
con2 = Con()
Log().write('con2 id= %d' %id(con2))
con2.db.execute('show processlist')
Log().write(con2.db.fetchall())

import copy

#Conexao3
con3 = Con()
Log().write('con1 id= %d' %id(con1))
con1.db.execute('show processlist')
Log().write(con1.db.fetchall())






