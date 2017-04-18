#!/usr/bin/python

#-*-coding: utf-8 -*-

import datetime
from datetime import date

"""datetime() - recebe como parametros: 
                   ano, mes, dia, hora, minuto e segundo
   e retorna um objeto do tipo datetime"""
dt = datetime.datetime(2020, 12, 31, 23,59,59)

#objetos date e time podem ser criados a partir  de um objeto datetime
data = dt.date()
hora = dt.time()

#quanto tempo falta para 2020
dd =  dt - dt.today()

#hora atual
hoje = date.today()

print 'Data: ',data
print 'Hora: ',hora
print 'Quanto tempo falta para 2020: ', str(dd).replace('days','dias')
print 'Hoje eh: ',hoje
