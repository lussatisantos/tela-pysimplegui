import PySimpleGUI as sg

sg.theme('dark')

class TelaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0), key='nome')],
            [sg.Text('idade', size=(5,0)),sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de email sao aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Button('Enviar dados')]
        ]
        # janela
        janela = sg.Window('Dados do Usuario', ).layout(layout)
        # extrair dados da tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        aceita_gmail = self.values['gmail']
        aceita_outlook = self.values['outlook']
        aceita_yahoo = self.values['yahoo']
        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'aceita gmail: {aceita_gmail}')
        print(f'aceita outlook: {aceita_outlook}')
        print(f'aceita yahoo: {aceita_yahoo}')

tela = TelaPython()
tela.Iniciar()