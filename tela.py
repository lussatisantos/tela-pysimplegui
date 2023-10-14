import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Nome'),sg.InputText],
            [sg.Text('idade'),sg.InputText],
            [sg.Button('Enviar dados')]
        ]
        # janela
        janela = sg.Window("Dados do Usuario").layout(layout)
        # extrair dados da tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.inicar()