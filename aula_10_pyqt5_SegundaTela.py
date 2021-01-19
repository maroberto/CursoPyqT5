from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


# médodo chama segunda tela e fecha a primeira
def chama_segunda_tela():
    segunda_tela.show()
    QMessageBox.about(segunda_tela, 'Alerta', 'você está na segunda tela!')
    primeira_tela.close()


# método chama a primeira tela e fecha a segunda
def chama_primeira_tela():
    primeira_tela.show()
    QMessageBox.about(primeira_tela, 'Alerta', 'você está na primeira tela!')
    segunda_tela.close()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi('ui/aula_10a.ui')
segunda_tela = uic.loadUi('ui/aula_10b.ui')


# conecta os botões das telas aos metodos
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(chama_primeira_tela)


primeira_tela.show()  # faz a primeira abertura da tela
app.exec()
