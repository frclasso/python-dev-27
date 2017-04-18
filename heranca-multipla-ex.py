#!/usr/bin/python

# -*-coding: utf-8 -*-

class Terrestre(object):
    """Classe de veiculos terrestres"""
    se_move_em_terra =True
    def __init__ (self, velocidade=100):
        """inicializa o objecto"""
        self.velocidade_em_terra = velocidade

class Aquatico(object):
    """Class dos veiculos aquaticos"""
    se_move_na_agua = True
    def __init__(self, velocidade=5):
        """inicializa o objeto"""
        self.velocidade__agua = velocidade


class Carro(Terrestre):
    """Classe de carros"""
    rodas = 4
    def __init__(self, velocidade=120, pistoes=4):
        """inicializa o objeto"""
        self.pistoes = pistoes
        Terrestre.__init__(self, velocidade=velocidade)

class Barco(Aquatico):
    """classo de barcos"""
    def __init__(self, velocidade=6, helices=1):
        """inicializa o objeto"""
        self.helices = helices
        Aquatico.__init__(self, velocidade=velocidade)

class Anfibio(Carro, Barco):
    """Classe de anfibios"""
    def __init__(self, velocidade_em_terra=80, velocidade_na_agua=4, pistoes=6, helices=2):
        """inicializa o objeto"""
        #Precisamos invocar o __init__ da classe Pai
        Carro.__init__(self, velocidade=velocidade_em_terra, pistoes=pistoes)
        Barco.__init__(self, velocidade=velocidade_na_agua, helices=helices)

novo_anfibio = Anfibio()

for atr in dir(novo_anfibio):
    #se nao for um metodo especial
    if not atr.startswith('__'):
        print atr, '=', getattr(novo_anfibio, atr)
