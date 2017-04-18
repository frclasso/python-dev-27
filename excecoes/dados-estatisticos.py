#!/usr/bin/python
#coding: utf-8

import string

data = open('myText.txt', 'r').read()

print 'Numero de linhas:',len(data.splitlines())
print'*********************'
print 'Numero de palavras:',len(string.split(data))
print '********************'
print 'Quantidade de letras:', len(data)
