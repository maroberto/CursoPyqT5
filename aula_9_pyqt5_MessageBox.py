from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


# cria o médodo recupera texto
def recupera_nome():
    nome = mbox.lineEdit.text()
    print(nome)
    mbox.lineEdit.setText('')  # limpa o campo de texto
    if nome == '':
        QMessageBox.about(mbox, 'Alerta', 'Nenhum nome foi digitado!')  # mostra a messagem de alerta
    else:
        QMessageBox.about(mbox, 'Obrigado', 'Olá: ' + nome)


app = QtWidgets.QApplication([])
mbox = uic.loadUi('ui/aula_9.ui')  # chama o arquivo ui
mbox.pushButton.clicked.connect(recupera_nome)

mbox.show()
app.exec()
