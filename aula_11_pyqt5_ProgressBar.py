from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from time import sleep

valor = 0


# cria o médodo recupera texto
def incrementa_valor():
    global valor
    while (valor < 110):
        barra_progresso.progressBar.setValue(valor)
        valor = valor + 10
        sleep(1)


def zerar_valor():
    global valor
    valor = 0
    QMessageBox.about(barra_progresso, 'Alerta', 'Tem certeza que deseja apagar?')
    barra_progresso.progressBar.setValue(valor)


app = QtWidgets.QApplication([])
barra_progresso = uic.loadUi('ui/aula_11.ui')  # chama o arquivo ui
barra_progresso.pushButton.clicked.connect(incrementa_valor)
barra_progresso.pushButton_2.clicked.connect(zerar_valor)

barra_progresso.show()
app.exec()
