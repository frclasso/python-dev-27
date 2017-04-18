#!/usr/bin/python

#conding: utf-8

from xml.etree.ElementTree import Element,ElementTree

root = Element('Canino')
lobo = Element('Lobo')
raposa = Element('Raposa')
coiote = Element('Coiote')
cachorro = Element('Cachorro', name='Bandit', raca='Labrador', cor='Branco')

root.append(lobo)
root.append(raposa)
lobo.append(coiote)
lobo.append(cachorro)

ElementTree(root).write('caninos.xml')

