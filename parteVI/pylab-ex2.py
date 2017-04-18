#!/usr/bin/python

#coding:utf-8

from pylab import *

#dados
ent1 = arange(0., 7., .1)
sai1 = cos(ent1)
sai2 = sin(ent1)
dif = sai2 -sai1

#Divida a figura em duas linhas e uma coluna, selecionando a parte superior
subplot(211)

"""Plota a curva
   primeira curva : ent1, sai1, 'bo:'
   segunda curva: ent1, sai2, 'g' 
"""
plot(ent1, sai1, 'bo:', ent1, sai2, 'g^-')

   #cria uma legenda
legend(['Cossenos', 'Senos'])

   #seleciona a parte inferior
subplot(212)

"""Desenha barras
      Eixo X: arange(len(dif)) + .5
      Eixo Y: dif
      Largura das barras: .5
      cor: #ccbbaa
"""
bar(arange(len(dif))+ .5, dif, .5, color='#ccbbaa')

#salva a figura
savefig('graf.png')