#!/usr/bin/python

#coding:utf-8

import xml.sax

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		xml.sax.handler.ContentHandler.__init__(self)
		self.prefixo = ''

	#eh chamado quando uma nova tag eh encontrada
	def startElement(self, tag, attr):
	    self.prefixo += ''	
	    print self.prefixo + "Elemento: ", tag
	    for item in attr.items:
	    	print self.prefixo + '- %s: %s' % item

	def characters(self, txt):
		if txt.strip():
			print self.prefixo + 'txt: ', txt

	def endElement(self, name):
		self.prefixo = self.prefixo[:-2] 

parser = xml.sax.make_parser()
parser.setContentHandler(Handler())
parser.parse('caninos.xml')           	