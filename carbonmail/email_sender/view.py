# É onde fica o código para a interface gráfica.
# Tudo que existir de visual, vai ficar aqui!
# É principalmente aqui, que usaremos o PySimpleGUI!

import PySimpleGUI as sg

# Window => Janela
# Layout => O que vai mostrar na janela
#        => Ele é uma lista de listas
#           Cada sublista, é uma lista da janela
#           Cada elemento, é um componente visual

lista = ["Administradores", "Alunos"]

def get_layout():
    layout = [
        [
            sg.Text("Selecione o seu código"),
            sg.In(),
            sg.FileBrowse(
                "Selecione", file_types=( ("Códigos Python", "*.py") 
                ,) # file_types diz quais são os arquivos que ele vai aceitar
        ), # * significa qualquer coisa, então nesse caso "qualquer coisa.py"
    ],        
        [
            sg.Text("Selecione a lista de destinário"), 
            sg.Combo(lista, default_value=lista[1]),
        ],
        [
            sg.Text("Insira o título: "),
            sg.In(key="-Title-"),
        ],
        [
           sg.Text("Insira o conteúdo do e-mail:"),
           sg.MLine(key="-Content-"), 
        ],
        [
            sg.Button("Enviar", key="-Send-"),
            sg.Button("Gerenciar listas", key="-ListEditor-")
        ]
    ]
    
    return layout

def get_window():
    return sg.Window("Teste de janela", get_layout())