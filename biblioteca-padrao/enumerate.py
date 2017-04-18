#!/usr/bin/python

# -*-coding: utf-8 -*-

import sys, os.path

fn = raw_input('Nome do arquivo: ').strip()

if not os.path.exists(fn):
    print 'Tente novamente...'
    sys.exit()

for i, s in enumerate(open(fn)):
    print i + 1, s

