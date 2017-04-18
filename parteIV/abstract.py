#!/usr/bin/python

#coding: utf-8

from abc import ABCMeta , abstractmethod

class Nave(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def mover (self, x0, x1, v):
		pass

class Zeppelin(Nave):
    def mover(self, x0, x1, v):
        d = x1 - x0
        t = v*d 
        return t


class Hovercraft(Nave):
    pass

z = Zeppelin()
h = Hovercraft()

