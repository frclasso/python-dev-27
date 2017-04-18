#!/usr/bin/python

#-*-coding: utf-8 -*-

#Property de leitura e escrita

class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance =  alcance
        self.tempo =  tempo

    #calcula veocidade
    def getv(self):
        return  self.alcance / self.tempo

     #calcula tempo
    def setv(self, v):
        self.tempo = self.alcance / v

    #Define a propriedade
    velocidade = property(getv, setv)

moab = Projetil(alcance=10000, tempo=60)
print moab.velocidade

#mudando a velocidade
moab.velocidae = 350
print moab.tempo
