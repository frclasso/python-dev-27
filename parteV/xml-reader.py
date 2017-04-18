#!/usr/bin/python

#coding:utf-8

from xml.etree.ElementTree import ElementTree

tree = ElementTree(file='caninos.xml')
root = tree.getroot()

#lista elementos abaixo de root
print root.getchildren()

#encontra lobo
lobo = root.find('Lobo')

#encontra cachorro
cachorro = lobo.find('Cachorro')
print cachorro.tag, cachorro.attrib

#remove raposa
root.remove(root.find('Raposa'))
print root.getchildren()