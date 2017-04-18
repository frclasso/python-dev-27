#!/usr/bin/python

#coding: utf-8

from numpy import arange, cos, sin


#duas funcoes do numpy para processamento de sinais
from scipy.signal import cspline1d, cspline1d_eval

#duas funcoes do Matplotlib  para gerar um grafico
from pylab import  plot, show

x0 = arange(20)
y0 = cos(x0) * sin(x0 /2) #Y a partir de x
dx = x0 [1]-x0[0] #diferenca original
x1 = arange(-1, 21, 0.1)

#coeficiente para arranjo de uma dimensao
cj = cspline1d(y0)

#Avalia o Spline para um novo conjunto de pontos
y1 = cspline1d_eval(cj, x1, dx=dx, x0=x0[0])

plot(x1, y1, '-g', x0, y0, '^y') #Desenha
show() #Mostra o grafico