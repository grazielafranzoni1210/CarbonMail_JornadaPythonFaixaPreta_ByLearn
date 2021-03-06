# Arquivo usado para transformar a pasta em pacote.
# Ele é sempre executado ao importar esse pacote

import PySimpleGUI as sg
import os
import sys
import re

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

def string_null_or_empty(string):
    return not string or string.isspace() # aqui vai retornar se é None(vazia) de fato,
    # ou se por exemplo, a pessoa deu um monte de espaço, aí acabou ficando vazia dessa forma.
    
def check_email(email):
    pattern = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

    valid_email = re.match(pattern, email)

    return valid_email