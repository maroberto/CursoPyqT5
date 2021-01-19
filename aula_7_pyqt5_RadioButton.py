from PyQt5 import uic, QtWidgets


def funcao_principal():
    if formulario.radioButton.isChecked():
        opcao = ('Opção verde selecionada')
        print('Opção verde selecionado')
    elif formulario.radioButton_2.isChecked():
        opcao = 'Opção vermelho selecionada'
        print('Opção vermelho selcionado')
    elif formulario.radioButton_3.isChecked():
        opcao = 'Opção amarelo selecionada'
        print('Opção amarelo selcionado')
    elif formulario.radioButton_4.isChecked():
        opcao = 'Opção branco selecionada'
        print('Opção branco selecionado')
    else:
        opcao = 'Nenhuma opção selecionada'
        print('Selecione uma opção')

    formulario.label_2.setText(opcao)


app = QtWidgets.QApplication([])
formulario = uic.loadUi('ui/aula_7.ui')
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
