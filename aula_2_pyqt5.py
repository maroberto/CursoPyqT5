import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


def QualNome(self):
    nome = str(input('Qual é seu nome? '))
    return ('Parabéns {} seu nome é muito bonito!'.format(nome))


def __init__(self):
    self.QualNome()


class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira Janela'

        botao1 = QPushButton('Botão 1', self)
        botao1.move(100, 450)
        botao1.resize(150, 50)
        botao1.setStyleSheet('QPushButton {background-color:#A9BCF5; font:bold; font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(550, 450)
        botao2.resize(150, 50)
        botao2.setStyleSheet('QPushButton {background-color:#A9BCF5; font:bold; font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('Botão 1 foi clicado')

    def botao2_click(self):
        print(QualNome(self))


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
