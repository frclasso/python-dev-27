#!/usr/bin/python

# -*- coding: latin1 -*-
"""
Um relogio com GTK.
"""
import datetime
# GTK e outros modulos associados
import gtk
import gtk. glade
import gobject
import pango


class Relogio( object):
    """
   Implementa a janela principal do programa.
    """
    def __init__( self):
    """
		Inicializa a classe.
		"""
        self. tree = gtk. glade. XML( 'relogio.glade', 'main')
        callbacks = {
		'on_main_destroy': self.on_main_destroy,
		'on_imagemenuitem5_activate': self.on_main_destroy,
		'on_imagemenuitem10_activate': self.on_imagemenuitem10_activate
		}
        self. tree. signal_autoconnect( callbacks)
        # Coloca um titulo na janela
		self. tree. get_widget( 'main').set_title( 'Relogio')
        # O rotulo que rebera a hora
		self. hora = self. tree. get_widget( 'lbl_hora')
        # A barra de status que rebera a data
		self. data = self. tree. get_widget( 'sts_data')
        print dir( self. data)
        # Muda a fonte do rotulo
		self. hora. modify_font( pango. FontDescription( 'verdana 28'))
        # Um temporizador para manter a hora atualizada
		self. timer = gobject. timeout_add( 1000, self. on_timer)

    def on_imagemenuitem10_activate(self, widget):
        """
		Cria a janela de "Sobre".
		"""
        # Caixa de dialogo
		dialog = gtk. MessageDialog( parent= self. tree. get_widget( 'main'),
		flags= gtk. DIALOG_MODAL | gtk. DIALOG_DESTROY_WITH_PARENT,
		type= gtk. MESSAGE_OTHER, buttons= gtk. BUTTONS_OK,
		message_format= 'Primeiro exemplo usando GTK.')
        dialog. set_title( 'Sobre')
        dialog. set_position( gtk. WIN_POS_CENTER_ALWAYS)
        # Exibe a caixa
		dialog. run()
        dialog. destroy()
        return
 

    def on_timer(self):
        #rotina para o temporizador
    	#pega a hora do sistema
		hora = datetime.datetime.now().time().isoformat().split('.')[0]

# Muda o texto do rotulo
		self. hora. set_text( hora)
        # Pega a data do sistema em formato ISO
		data = datetime. datetime. now().date().isoformat()
        data = 'Data: ' + '/'. join( data. split( '-')[::-1 ])
        # Coloca a data na barra de status
		self. data. push( 0 , data)
        # Verdadeiro faz com que o temporizador rode de novo
		return True

    def on_main_destroy(self, widget):
        #termina o programa
        raise SystemExit

if __name__ == '__main__':
    #inicia a GUI
    relogio = Relogio()
    gtk.main()    	
