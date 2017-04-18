#!/usr/bin/python

import traceback

try:
    fn = raw_input('Nome do arquivo: ').strip()
    for i, s in enumerate(file(fn)):
        print i + 1, s,
except:
    #exibe na tela
    trace = traceback.format_exc()
    print 'Aconteceu um erro:\n', trace
    #salva em um arquivo de log
    file('trace.log', 'a').write(trace)
   
    #encerra o programa
    raise SystemExit

