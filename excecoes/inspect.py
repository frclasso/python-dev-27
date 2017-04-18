#!/usr/bin/python

#-*- coding: utf-8 -*-
import os.path
import inspect

print 'Objeto: ', inspect.getmodule(os.path)
print 'Classe: ', inspect.isclass(str)

#lista todas as funcoes que existem em os.path
print 'Membros:'
for name, struct in inspect.getmembers(os.path):
    if inspect.isfunction(struct):
        print name,
