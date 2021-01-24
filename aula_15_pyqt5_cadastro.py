from PyQt5 import uic, QtWidgets
import sqlite3


def visualizar():
    cadastros_b.show()
    print('visualizar')
    banco = sqlite3.connect('banco_cadastro.sqlite3')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    cadastros_b.tableWidget.setRowCount(len(dados_lidos))
    cadastros_b.tableWidget.setColumnCount(3)
    print(dados_lidos)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            cadastros_b.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    banco.close()


def salvar_dados():
    print('salvar')
    nome = cadastro.lineEdit.text()
    endereco = cadastro.lineEdit_2.text()
    email = cadastro.lineEdit_3.text()

    try:
        banco = sqlite3.connect('banco_cadastro.sqlite3')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (nome text, endereco text, email text)")
        cursor.execute("INSERT INTO dados VALUES ('"+nome+"', '"+endereco+"', '"+email+"')")
        banco.commit()
        banco.close()
        cadastro.lineEdit.setText('')
        cadastro.lineEdit_2.setText('')
        cadastro.lineEdit_3.setText('')
        print('Dados inseridos com sucesso')

    except sqlite3.Error as erro:
        print('Erro ao inserir os dados: ', erro)


app = QtWidgets.QApplication([])
cadastro = uic.loadUi('ui/cadastro.ui')
cadastros_b = uic.loadUi(('ui/cadastro_b.ui'))
cadastro.pushButton.clicked.connect(salvar_dados)
cadastro.pushButton_2.clicked.connect(visualizar)

cadastro.show()
app.exec_()
