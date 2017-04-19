#!/usr/bin/python

import subprocess, gtk, gtk.glade, gobject, pango


class Exec(object):

    #janela principal
    def __init__(self):
        #carrega a interface
        self.tree = gtk.glade.XML('cmd.glade', 'main')

        #liga os eventos
        callbacks = {
            'on_main_destroy': self.on_main_destroy,
            'on_btn_fechar_clicked': self.on_main_destroy,
            'on_btn_rodar_clicked': self.on_btn_rodar_clicked
        }
        self.tree.signal_autoconnect(callbacks)

    def on_btn_rodar_clicked(self, widget):
        #roda o comando
        ntr_cmd = self.tree.get_widget('ntr_cmd')
        chk_shell = self.tree.get_widget('chk_shell')

        cmd = ntr_cmd.get_text()
        if cmd:
            #chk_shell.state sera 1 se chk_shell estiver marcado
            if chk_shell.state:
                cmd = 'cmd start cmd/c' + cmd
            subprocess.Popen(args=cmd)

        else:
            #caixa de dialogo
            dialog = gtk.MessageDialog(parent=self.tree.get_widget('main'),
                flags=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                type=gtk.MESSAGE_OTHER, buttons=gtk.BUTTONS_OK,
                message_format='Digite um comando.')

            dialog.set_title('Mensagem')
            dialog.set_position(gtk.WIN_POS_CENTER_ALWAYS)

            #exibe a caixa
            dialog.run()
            dialog.destroy()

        return True

    def on_main_destroy(self, widget):
        #terminan o programa
        raise SystemExit


if __name__ == "__main__":
    #inicia a GUI
    exe = Exec()
    gtk.main()
