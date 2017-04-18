#!/usr/bin/python

#coding: utf-8

import time

def logger(cls):
	"""Funcao decoradora classe"""
	class logged(cls):
		"""Classe derivada que exibe os paramentros de inicializacao"""
		def __init__(self, *args, **kwargs):
			print 'Hora: ', time.asctime()
			print 'Classe: ', repr(cls)
			print 'args: ', args
			print 'kwargs: ', kwargs

			#executa a inicializacao da classe antiga
			cls.__init__(self, *args, **kwargs)
	return logged
	
@logger
class Musica(object):
    def __init__(self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album

m = Musica('Hand of Doom', 'Balck Sabbath', album='Paranoid')
			