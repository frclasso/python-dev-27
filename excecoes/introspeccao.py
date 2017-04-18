#!/usr/bin/pyton

#-*-coding: utf-8 -*-
"""
   colhendo informacoes de objetos globais no programa
"""
from types import ModuleType

def info(n_obj):
    #cria uma referencia ao objeto
    obj = globals()[n_obj]
    #exibe infos sobre objeto
    print 'Nome do objeto: ', n_obj
    print 'Identificador:  ', id(obj)
    print 'Tipo: ', type(obj)
    print 'Representacao: ', repr(obj)

    #se for um modulo
    if isinstance(obj, ModuleType):
        print 'itens: '
        for item in dir(obj):
            print item
        print

#exibindo as informacaoes
for n_obj in dir():
    info(n_obj)
