# Arquivo usado para transformar a pasta em pacote.
# Ele é sempre executado ao importar esse pacote

import PySimpleGUI as sg
# um evento pra saber quando o PySimpleGUI fechou a janela pra gente
from PySimpleGUI import WIN_CLOSED
from carbonmail.email_sender import view
from carbonmail.list_editor.manager import initialize as init_list_editor

class Email_Sender():
    def __init__(self):
        self.window = None
        
    def instantiate(self): # vai criar a janela
        if self.window == None:
            self.window = view.get_window()
        

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if event == WIN_CLOSED:  # se o usuário clicou no x, vai fechar a janela
                self.close_window()
                break  # para sair do laço de repetição do while

            elif event == "-Send-":
                title = values["-Title-"]
                content = values["-Content-"]

                sg.Popup(
                    f'O título é: {title}\nO conteúdo é: {content}', # \n é uma quebra de linha
                    title='E-mail',
                )
            
            elif event == "-ListEditor-":
                self.hide_window()
                init_list_editor(self)
    
    def close_window(self):
        if self.window != None:
           self.window.Close()
           
    def hide_window(self):
        if self.window != None:
            self.window.Hide()
    
    def unhide_window(self):
        if self.window != None:
            self.window.Unhide()