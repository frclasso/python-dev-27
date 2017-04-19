#!/usr/bin/python

# -*-coding:utf-8 -*-

import wx

class Main(wx.Frame):
    #classe que define a janela principal do programa
    def __init__(self, parent, id, title):
        #inicializa a classe
        #define a janela usando o __init__ da class mae
        wx.Frame.__init__(self,parent, id, title, size=(600, 400))

        #cria uma caixa de texto
        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        #pega a fonte do programa decodificando para latin1
        font = file(__file__, 'rb').read().decode('latin1')

        #carrega o fonte do programa na caixa de texto
        self.text.SetLabel(font)

        #exibe janela
        self.Show(True)

if __name__ == '__main__':
    #cria um objeto de aplicacao  do wxPython
    app = wx.App()

    #cria um objeto 'janela' a partir da classe
    frame = Main(None, wx.ID_ANY, 'Fonte')

    #inicia o loop de tratamento de eventos
    app.MainLoop()

