# Arquivo usado para transformar a pasta em pacote.
# Ele é sempre executado ao importar esse pacote

import PySimpleGUI as sg

def inner_element_space(width=100):
    return [sg.Text(" " * width, font=("Arial", 1))]