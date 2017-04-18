#!/usr/bin/python

# -*-coding: utf-8 -*-

class Mat(object):
    """Matriz esparsa"""
    def __init__(self):
        #inicia a matriz
        self.itens = []
        self.default =0

    def __getitem__(self, xy):
        """Retorna o item X e Y ou default caso contrario"""
        i = self.index(xy)
        if i is None:
            return self.default

        return self.itens [i][-1] 

    def __setitem__(self, xy, data=0):
        #Cria um novo item na matriz
        i = self.index(xy)
        if not i is None:
            self.itens.pop(i)
        self.itens.append((xy, data))

    def __delitem__(self, xy):
        #Remove um item da matriz
        i = self.index(xy)
        if i is None:
            return self.default
        return self.itens.pop(i)

    def __getslices__(self, x1, x2):
        #Seleciona linhas da matriz
        r = []
        for i in xrange(x1, x2 + 1):
            r.append(self.row(x))
        return r

    def index(self, xy):
        i =0
        for item in self.itens:
            if xy == item[0]:
                return i
            i += 1
        else:
            return None

    def dim(self):
        #Retorna as dimensoes atuais da matriz
        x = y = 0
        for xy, data in self.itens:
            if xy[0] > x:x = xy[0]
            if xy[1] > y:y = xy [1]
        return x,y

    def keys(self):
        #Retorn as coordenadas preenchicas
        return [xy for xy, data in self.itens]

    def values(self):
        #Retorna valores preechidos
        return [data for xy, data in self.itens]

    def row(self, x):
        #Retorna linha especificada
        X, Y = self.dim()
        r = []
        for y in xrange(1, Y + 1):
            r.append(self[x,y])
        return r

    def col(self, y):
        #Retorna a coluna especificada
        X,Y = self.dim()
        r = []
        for x in xrange(1, X + 1):
            r.append(self[x,y])
        return r

    def sum(self):
        #Calcula somatorio
        return sum(self.values())

    def avg(self):
        #Calcula media
        X,Y = self.dim()
        return self.sum() /(X * Y)

    def __repr__(self):
        """Retorna a representacao do objeto como texto"""
        r = 'Dim: %s\n' % repr(self.dim())
        X, Y  = self.dim()
        for x in xrange(1, X + 1):
            for y in xrange(1, Y + 1):
                r += ' %s = %3.1f' % (repr((x,y)),
                    float(self.__getitem__((x,y))))
            r += '\n'
        return r

if __name__ == '__main__':
    mat = Mat()
    print '2 itens preechidos: '
    mat[1,2] = 3.14
    mat[3,4] = 4.5
    print mat

    print 'Troca  e remocao: '
    del mat[3,4]
    mat[1,2] = 5.4
    print mat

    print 'Preechendo a 3a coluna'
    for i in xrange(1,4):
        mat[i + 1,3] = 1
    print mat

    print '3a coluna: ', mat.col(3)
    print 'Fatias com a 2a e 3a linhas', mat[2:3]
    print 'Somatorio: ', mat.sum(), 'Media: ', mat.avg()
            
