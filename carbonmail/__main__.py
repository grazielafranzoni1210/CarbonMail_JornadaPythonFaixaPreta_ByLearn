# Arquivo principal (inicial) a ser executado.
# Quando iniciamos o projeto (carbonmail), ele é o primeiro que o Python vai executar.
# Nós usamos também para ser o ponto de entrada da aplicação

from carbonmail.email_sender import view

# Depois vamos colocar no manager do email_sender
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED # um evento pra saber quando o PySimpleGUI fechou a janela pra gente

def enable_window():
    window = view.get_window()
    
    while True:
        event, values = window.read()
        
        if event == WIN_CLOSED: # se o usuário clicou no x, vai fechar a janela
            window.close()
            break # para sair do laço de repetição do while

enable_window()