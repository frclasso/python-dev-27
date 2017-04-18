#!/usr/bin/python

#coding:utf-8
#Gera a figura mapa1.png

"""Before you need install mpl_tookits.basemap
apt-get install python-mpltoolkits.basemap
"""

from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot
from numpy import arange

#cria um mapa usando Basemap
mapa = Basemap(projection='robin', lat_0=20, lon_0=-50,
	resolution='l', area_thresh=1e3)


#desenha  a costa dos continentes
mapa.drawcoastlines(color='#777799')

#desenha as fronteiras
mapa.drawcountries(color='#ccccee')

#pinta os continentes
mapa.fillcontinents(color='#ddddcc')

#desenha os meridianos
mapa.drawmeridians(arange(0, 360, 30), color='#ccccee')

#desenha os paralelos
mapa.drawparallels(arange(-180, 180, 30), color='#ccccee')

#desenha os limites dos mapas
mapa.drawmapboundary()

#salva imagem
pyplot.savefig('mapa1.png', dpi=150)