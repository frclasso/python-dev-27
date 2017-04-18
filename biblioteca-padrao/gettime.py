#!/usr/bin/python

import time

"""localtime()  - retorna  data e hora local no formato
   de uma estrutura chamada struct_time, ano, mes, dia, hora, minuto,
   segundo, dia da semana,  dia no ano e horario de verao """

print time.localtime()	

#asctime() - retorna data e hora como string, conforme a config do OS
print time.asctime()



#time() - retorna o tempo do sistema em segundos
ts1=  time.time()

#gmtime() - converte segundos para struct_time
tt1 = time.gmtime(ts1)
print ts1, '->', tt1

#somando uma hora
tt2 = time.gmtime(ts1 + 3600)

#mktime()  - converte strct_time para segundos
ts2 = time.mktime(tt2)
print ts2, '->', tt2

#clock() - retorna o tempo da aplicacao
print 'O programa levou', time.clock(), 'segundos ate agora'

for i in xrange(5):
    time.sleep(1)
    print i + 1, 'segundo(s)'


