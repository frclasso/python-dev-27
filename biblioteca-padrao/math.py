#!/usr/bin/python

#coding: utf-8

import math, cmath

"""modulos para matematica e para matematica com numeros complexos"""
for cpx in [3j, 1.5+1j, -2 -2j]:
    plr = cmath.polar(cpx)
    print 'Complexo: ', cpx
    print 'Forma polar: ', plr, '(em radianos)'
    print 'Amplitude: ', abs(cpx)
    print 'Angulo: ',math.degrees(plr[1]), '(graus)'
