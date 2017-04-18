#!/usr/bin/python

#coding: utf-8
import numpy

#criando arranjos
print 'Arranjo criado a partir de uma lista'
a = numpy.array([0,1,2,3,4,5,6,7,8,9])

print a

print '*************************************'
print 'Arranjo criado a partir  de um intervalo'
z = numpy.arange(0., 4.5, .5)
print z

print '*************************************'
print "Arranjo  de 1's 2x3"
y = numpy.ones((2,3))
print y

print '*************************************'
print 'Arranjo podem gerar novos arranjos:'
cos = numpy.round(numpy.cos(z), 1)
print cos

print '*************************************'
print 'Multiplicando  cada elemento por um escalar:'
print 5 * z

print '*************************************'
print 'Somando arranjos elemento por elemento:'
print z + cos

print '*************************************'
print 'Redimensionando o arranjo:'
z.shape = 3, 3
print z

print '*************************************'
print ' Arranjo tranposto:'
print z.transpose()

print '*************************************'
print 'Achatando o arranjo:'
print z.flatten()

print '*************************************'
print 'O acesso aos elementos funciona como nas listas'
print z[1]

print '*************************************'
print 'Caso especial, diferente das listas:'
print z[1, 1]

print '*************************************'
#Dados sobre o arranjo
print 'Formato do arranjo:'
print z.shape

print '*************************************'
print 'Quantidade de eixos:'
print z.ndim

print 'Tipo de dados:'
print z.dtype