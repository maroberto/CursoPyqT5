from PyQt5 import uic, QtWidgets
# cria lista em branco
lista_nomes = []


# cria função e captura e mostra os dados na tela
def listar_dados():
    dados_digitados = lista.lineEdit.text()
    print(dados_digitados)
    lista.listWidget.addItem(dados_digitados)
    lista.lineEdit.setText("")

    # adiciona itens digitados na lista_nomes
    lista_nomes.append(dados_digitados)
    print(lista_nomes)


# apaga dados da tela e da lista_nomes
def deletar():
    lista.listWidget.clear()
    lista_nomes.clear()
    print('Deletar')


# inicia a tela
app = QtWidgets.QApplication([])
lista = uic.loadUi('ui/aula_8.ui')
lista.pushButton.clicked.connect(listar_dados)
lista.pushButton_2.clicked.connect(deletar)

lista.show()
app.exec()
