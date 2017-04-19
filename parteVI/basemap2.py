#!/usr/bin/python

#coding:utf-8

from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot

mapa = Basemap(projection='ortho', lat_0=10, lon_0=-10,
	resolution='l', area_thresh=1e3)

#preeche com relevo
mapa. bluemarble()
mapa. drawmapboundary()

lxy = (('Gntech\nFloripa\nBrasil', -48.54, -27.59),
	('Londres', 0.07, 50.30))

#transposta
lxy = zip(*lxy)

#converte as coordenadas
x,y = mapa(lxy[1], lxy[2])
lxy = lxy[0],x,y

#marca no mapa
mapa.plot(x,y,'w^')

#escreve os nomes
for l, x, y in zip(*lxy):
	pyplot.text(x+2e5, y-6e5, l,
		color='#eeeecc')

pyplot.savefig('mapa2.png', dpi=150)