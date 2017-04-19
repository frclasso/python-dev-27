#!/usr/bin/python

#-*-coding:latin1 -*-

import wx, time


class Main(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(150, 80))
        clock = time.asctime().split()[3]

        #cria um rotulo do texto
        self.control = wx.StaticText(self, label=clock)

        #muda a fonte
        self.control.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD))

        #cria timer
        TIMER_ID = 100
        self.timer = wx.Timer(self, TIMER_ID)

        #inicia o timer
        self.timer.Start(1000)

        #Associa  os metodos com os eventos
        wx.EVT_TIMER(self, TIMER_ID, self.on_timer)
        wx.EVT_CLOSE(self, self.on_close)
        self.Show(True)

    def on_timer(self, event):
        #atualiza relogio
        clock = time.asctime().split[3]
        self.control.SetLabel(clock)

    def on_close(self, event):
        #para o timer
        self.timer.Stop()
        self.Destroy()


app = wx.App()
Main(None, wx.ID_ANY, 'Relogio')
app.MainLoop()