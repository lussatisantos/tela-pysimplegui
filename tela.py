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
            [sg.Text('Aceita Cartao')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Nao', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(15, 20), key='slidervelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30, 20))]
        ]
        # janela
        self.janela = sg.Window('Dados do Usuario', ).layout(layout)
        # extrair dados da tela
        self.button, self.values = self.janela.Read()
    
    def Iniciar(self):
        while True:
            # extrair dados da tela
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['slidervelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'Aceita cartao: {aceita_cartao}')
            print(f'Nao aceita cartao: {nao_aceita_cartao}')
            print(f'Velocidade script: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()