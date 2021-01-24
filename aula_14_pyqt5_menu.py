from PyQt5 import uic, QtWidgets


def menu_verde():
    menu.label_2.setText('Verde')
    menu.label_2.setStyleSheet('color: green')
    print('Verde')


def menu_azul():
    menu.label_2.setText('Azul')
    menu.label_2.setStyleSheet('color: blue')
    print('Azul')


def menu_vermelho():
    menu.label_2.setText('Vermelho')
    menu.label_2.setStyleSheet('color: red')
    print('Vermelho')


app = QtWidgets.QApplication([])
menu = uic.loadUi('ui/aula_14.ui')

menu.actionVermelho.triggered.connect(menu_vermelho)
menu.actionAzul.triggered.connect(menu_azul)
menu.actionVerde.triggered.connect(menu_verde)
menu.show()
app.exec_()
