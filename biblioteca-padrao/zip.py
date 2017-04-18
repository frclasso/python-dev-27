#!/usr/bin/python

# -*- coding: utf-8 -*-

""" Gravando texto em um arquivo compactado"""
import zipfile

texto = """
*********************************************************
Esse texto sera compactado e guardado em um arquivo zip.
*********************************************************
"""

#cria um nov arquivo zip
zip = zipfile.ZipFile('arq.zip','w', zipfile.ZIP_DEFLATED)

#escfreve uma string no zip
zip.writestr('texto.txt', texto)
zip.close()
