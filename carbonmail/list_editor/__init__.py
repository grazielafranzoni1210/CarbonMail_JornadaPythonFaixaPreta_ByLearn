# Arquivo usado para transformar a pasta em pacote.
# Ele é sempre executado ao importar esse pacote

import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.list_editor import view

class List_Editor:
    def __init__(self, email_sender):
        self.window = None
        self.ems = email_sender

    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if event in (WIN_CLOSED, '-Back-'): # dois eventos acontecendo na mesma ação
                self.window.close() # event com in, verifica se está ou em WIN_CLOSED ou em Back
                self.ems.unhide_window()
                break
            
            if event == "-Send-":
                title = values["-Title-"]
                content = values["-Content-"]
                
                sg.Popup(
                    f'O título é: {title}\nO conteúdo é: {content}', # \n é uma quebra de linha
                    title='E-mail',
                )    

    def close_window(self):
        if self.window is not None:
            self.window.Close()
        self.window = None

    def hide_window(self):
        if self.window != None:
            self.window.Hide()

    def unhide_window(self):
        if self.window != None:
            self.window.UnHide()