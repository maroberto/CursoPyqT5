import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from UsoQTableWidgetDialog import UsoTableWidgetDialog


class UsoQTableWidgetApplication(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = UsoTableWidgetDialog()
        self.ui.setupUi(self)

        self.inicializar_dados()

        self.agregar_conteudo()

        self.show()

    def inicializar_dados(self):
        self.dados = []

        self.dados.append(('Python', '3.7.3'))
        self.dados.append(('Java', '8'))
        self.dados.append(('PHP', '7.3'))
        self.dados.append(('c#', '8'))
        self.dados.append(('C++', '17'))
        self.dados.append(('HTML5', '5'))

    def agregar_conteudo(self):

        linha = 0

        for registro in self.dados:
            coluna = 0
            self.ui.tbl_linguagens.insertRow(linha)
            for elemento in registro:
                ceta = QTableWidgetItem(elemento)
                self.ui.tbl_linguagens.setItem(linha, coluna, ceta)
                coluna += 1
            linha += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = UsoQTableWidgetApplication()
    janela.show()
    sys.exit(app.exec_())
