import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui


def QualNome(self):
    nome = str(input('Qual é seu nome? '))
    return ('Parabéns {} seu nome é muito bonito!'.format(nome))


def __init__(self):
    self.QualNome()


class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        # cria janela
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira Janela'
        # cria caixa de texto(textbox)
        self.text_box = QLineEdit(self)
        self.text_box.move(580, 50)
        self.text_box.resize(200, 30)
        self.text_box.setStyleSheet('QLineEdit {font:bold; font-size:20px; color:#FA5858}')
        self.text_box.setText('Digite seu nome')
        # cria botão 1, 2, 3
        botao1 = QPushButton('Java', self)
        botao1.move(100, 450)
        botao1.resize(150, 50)
        botao1.setStyleSheet('QPushButton {background-color:#A9BCF5; font:bold; font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Python', self)
        botao2.move(550, 450)
        botao2.resize(150, 50)
        botao2.setStyleSheet('QPushButton {background-color:#A9BCF5; font:bold; font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        botao_nome = QPushButton('Enviar', self)
        botao_nome.move(610, 90)
        botao_nome.resize(140, 40)
        botao_nome.setStyleSheet('QPushButton {background-color:#A9BCF5; font:bold; font-size:20px}')
        botao_nome.clicked.connect(self.botao_nome_click)
        # cria label1, label_nome
        self.label_1 = QLabel(self)
        self.label_1.setText('Olá usuario, seja bem vindo! Qual é seu nome: ')
        self.label_1.move(30, 47)
        self.label_1.resize(700, 30)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color: #FA5858}')

        self.label_nome = QLabel(self)
        self.label_nome.setText('')
        self.label_nome.move(30, 80)
        self.label_nome.resize(700, 30)
        self.label_nome.setStyleSheet('QLabel {font:bold; font-size:25px; color:#FA5858}')
        # inseri as imagens
        self.logo = QLabel(self)
        self.logo.move(210, 200)
        self.logo.setPixmap(QtGui.QPixmap('imagens/python-logo-5.png'))
        self.logo.resize(420, 150)
        # cria a janela
        self.CarregarJanela()

    # mostra a janela
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    # função de click's botões 1, 2 e nome
    def botao1_click(self):
        print('Botão 1 foi clicado')
        self.label_1.move(300, 50)
        self.label_1.setText('Click no botão Python')
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color: #5882FA}')
        self.logo.move(390, 200)
        self.logo.setPixmap(QtGui.QPixmap('imagens/java-logo-13.png'))

    def botao2_click(self):
        print('Botão 2 foi clicado')
        self.label_1.move(300, 50)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color: #FF8000}')
        self.label_1.setText('Click no botão Java')
        self.logo.setPixmap(QtGui.QPixmap('imagens/python-logo-5.png'))
        self.logo.move(210, 200)

    # função recupera texto do botão
    def botao_nome_click(self):
        conteudo = self.text_box.text()  # esse comando recupera o que foi digitado na caixa de texto
        self.label_1.setText('Seja bem vindo {}!'.format(conteudo))


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
