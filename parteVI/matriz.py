#!/usr/bin/python

import numpy

print 'Criando uma matriz a partir de uma lista:'
l = [[3,4,5], [6,7,8], [9,0,1]]
Z = numpy.matrix(l)

print Z
print '*************************************'

print 'Transposta da matriz:'
print Z.T

print '*************************************'
print  'Inversa da matriz:'
print Z.I

print '*************************************'

#criando outra matriz
R = numpy.matrix([[3,2,1]])

print 'Multiplicando  matrizes:'
print R * Z

print '*************************************'

print 'Resolvendo um problema linear:'
print numpy.linalg.solve(Z, numpy.array([0,1,2]))