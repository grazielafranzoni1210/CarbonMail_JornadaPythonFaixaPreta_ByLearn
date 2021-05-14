# É onde fica o código para a interface gráfica.
# Tudo que existir de visual, vai ficar aqui!
# É principalmente aqui, que usaremos o PySimpleGUI!

import PySimpleGUI as sg

# Window => Janela
# Layout => O que vai mostrar na janela
#        => Ele é uma lista de listas
#           Cada sublista, é uma lista da janela
#           Cada elemento, é um componente visual

def get_layout():
    layout = [
        [sg.Text("Eu sou um texto")],
        [sg.Text("Eu sou um texto"), sg.Button("Eu sou um botão")],
    ]
    
    return layout

def get_window():
    return sg.Window("Teste de janela", get_layout())