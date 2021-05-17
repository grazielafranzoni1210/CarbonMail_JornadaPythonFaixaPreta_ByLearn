# Arquivo usado para transformar a pasta em pacote.
# Ele é sempre executado ao importar esse pacote

import PySimpleGUI as sg
import os
import sys

def inner_element_space(width=100):
    return [sg.Text(" " * width, font=("Arial", 1))]

def root_folder():
    try:
        main_file = os.path.abspath(sys.modules['__main__'].__file__) # modules são os scripts
        # então aqui vai pegar as propriedades do arquivo main
    except:
        main_file = sys.executable
    
    # retornando o diretório pai do arquivo main
    return os.path.join(os.path.dirname(main_file), os.pardir)