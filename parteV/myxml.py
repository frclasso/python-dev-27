#!/usr/bin/python

#coding:utf-8
import xml.dom.minidom

doc = xml.dom.minidom.Document()

#para ler um documento existente
#doc =xml.dom.minidom.parse('caninos.xml')

#cria elementos
root = doc.createElement('Canino')
lobo = doc.createElement('Lobo')
raposa = doc.createElement('Raposa')
coiote = doc.createElement('Coiote')
cachorro = doc.createElement('Cachorro')

#cria os atributos
cachorro.setAttribute('nome', 'Bandit')
cachorro.setAttribute('raca', 'Labrador')
cachorro.setAttribute('cor', 'Branco')


#cria a estrutura
doc.appendChild(root)
root.appendChild(lobo)
root.appendChild(raposa)
lobo.appendChild(coiote)
lobo.appendChild(cachorro)

print doc.toprettyxml()
