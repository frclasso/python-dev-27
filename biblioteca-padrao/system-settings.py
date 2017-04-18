#!/usr/bin/python

# -*- coding: utf-8 -*-
import os , sys, platform

def uid():
    """
      uid - retorn a identificacao do usuario corrente ou
      None quando nao for possivel encontrar
    """

#variaveis de ambiente para cada sistema operacional
    us = {'Windows':'USERNAME', 'Linux':'USER'}
    u = us.get(platform.system())
    return os.environ.get(u)
   
print 'Usuario: ', uid()
print 'Plataforma: ', platform.platform()
print 'Diretorio corrente: ', os.path.abspath(os.curdir)
exep, exef=os.path.split(sys.executable)
print 'Executavel: ', exef
print 'Diretorio do executavel: ', exep

