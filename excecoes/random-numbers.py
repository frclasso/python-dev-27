#!/usr/bin/python

#-*-coding: utf-8 -*-
import random

#cria um arquivo com 25 numeros randomicos
with file('temp.txt','w') as temp:
    for y in range(5):
        for x in range(5):
            #print grava a saida do comando no arquivo indicado
            print >> temp, '%.2f'% random.random(),
        print >> temp

#exibe o conteudo do arquivo
with file('temp.txt') as temp:
    for i in temp:
        print i,

#Fora dos blocos  o arquivo esta fechado
#isso gera uma excesao ValueError: I/O operation on closed file
