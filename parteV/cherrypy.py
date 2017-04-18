#!/usr/bin/python

import cherrypy

class Root(object):

	@cherrypy.expose
	
	def index(self):
		return 'Hello World!'

cherrypy.quickstart(Root())
