#!/usr/bin/python

# -*- coding: latin1 -*-

import urllib

url = urllib.urlopen('http://ark4n.wordpress.com/')
html = url.read()

found = html.find('href=', 0)

#find retorna -1 se nao encontra
while found >= 0:
	end = html.find(html[found + 5], found + 6)+1
	print html[found:end]

	#passa para o proximo link
	found = html.find('href=', found + 1)
