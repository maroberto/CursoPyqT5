from PyQt5 import uic, QtWidgets


def pegar_data():
    data = str(calendario.calendarWidget.selectedDate())
    data_formatada = (data[19:29])
    dia = (data[28:31])
    mes = (data[24:27])
    ano = (data[19:23])
    print(data_formatada)
    calendario.label.setText('Data selecionada: ' + dia + '/' + mes + '/' + ano)


app = QtWidgets.QApplication([])
calendario = uic.loadUi('ui/aula_12.ui')

calendario.calendarWidget.selectionChanged.connect(pegar_data)
calendario.show()
app.exec_()
