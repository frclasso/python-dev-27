#!/usr/bin/python
#coding:utf-8

from numpy import *

A = array([(9,4,2), (5,3,1), (2,0,7)])
print 'Matriz A:'
print A

print 'Decompondo usando QR:'
Q,R = linalg.qr(A)

#Resultados
print'Matriz Q:'
print Q

print 'Matriz R:'
print R

print 'Produto:'
print 'Q.R'
print int0(dot(Q, R))

