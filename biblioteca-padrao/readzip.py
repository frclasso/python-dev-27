#!/usr/bin/python

# -*-coding: utf-8 -*-
"""Lendo um arquivo zip"""
import zipfile
zip = zipfile.ZipFile('arq.zip')
arqs = zip.namelist()
for arq in arqs:
    print 'Arquivo: ',arq
    zipinfo = zip.getinfo(arq)
    print 'Tamanho original: ',zipinfo.file_size
    print 'Tamanho comprimido: ',zipinfo.compress_size
    print zip.read(arq)


