from PyQt5 import uic, QtWidgets


app = QtWidgets.QApplication([])
responsiva = uic.loadUi('ui/aula_13.ui')

responsiva.show()
app.exec_()
