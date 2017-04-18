#!/usr/bin/python

# -*-coding: latin1 -*-

from ZODB import FileStorage, DB
import transaction

#definindo o armazenamento do banco
storage = FileStorage.FileStorage('people.fs')
db = DB(storage)

conn = db.open()

#referencia para raiz da arvore
root = conn.root()

#um registro persistente
root['singer'] = 'Kate Bush'

#efetuando a alteracao
transaction.commit()
print root['singer'] #Kate Bush

#alterando um item
root['singer'] = 'Tori Amos'
print root['singer'] #Tori Amos

#abortando
transaction.abort()

#o item voltou ao que era antes da transacao
print root['singer'] #Kate Bush