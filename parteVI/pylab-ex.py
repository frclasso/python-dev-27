#!/usr/bin/python

#coding:utf-8

from pylab import *

ent = arange(0., 20.1,.1)

print "Calcula os cossenos das entradas"
sai = cos(ent)

print 'plota a curva'
plot(ent, sai)


print 'Texto para o eixo x'
xlabel('entrada')

print 'Texto para o eixo y'
ylabel('cosseno')

print 'Texto no topo da figura'
title('Cossenos')

print 'Ativa a grade'
grid(True)

#apresenta  a figura resultante na tela
show()