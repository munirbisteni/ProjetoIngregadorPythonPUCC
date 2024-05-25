import sys
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QMainWindow,
    QWidget,
)

from estoque import Estoque
from mensagemWindow import MensagemWindow
from .alterarEstoqueWindow import  AlterarEstoqueWindow


class ListarEstoqueWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listar Estoque")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.initUI()

    def initUI(self):
        self.populate_table()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    
    def populate_table(self):
        self.estoques = Estoque.listar_estoque()
        self.table_widget.setRowCount(len(self.estoques))
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["EstoqueID", "Ingrediente", "Data de validade", "Alterar", "Excluir"])

        for row, estoque in enumerate(self.estoques):
            lote_id_item = QTableWidgetItem(f"{estoque[0]}")
            self.table_widget.setItem(row, 0, lote_id_item)

            nome_item = QTableWidgetItem(f"{estoque[1]}")
            self.table_widget.setItem(row, 1, nome_item)

            data_producao_item = QTableWidgetItem(estoque[4].strftime("%d/%m/%Y"))
            self.table_widget.setItem(row, 2, data_producao_item)

            alterar_button = QPushButton("Alterar")
            alterar_button.clicked.connect(lambda _, e=estoque: self.alterar_estoque(e))
            self.table_widget.setCellWidget(row, 3, alterar_button)

            excluir_button = QPushButton("Excluir")
            excluir_button.clicked.connect(lambda _, e=estoque: self.excluir_estoque(e))
            self.table_widget.setCellWidget(row, 4, excluir_button)

    def alterar_estoque(self, estoque):
        self.selectedOption = AlterarEstoqueWindow(estoque)
        self.selectedOption.window_closed.connect(self.populate_table)
        self.selectedOption.show()

        print(f"Alterar Estoque: {estoque}")

    def excluir_estoque(self, estoque):
        Estoque.excluir_estoque(estoque[0])
        self.msg = MensagemWindow(False,f"Estoque de id {estoque[0]} excluído com sucesso")
        self.msg.show()
        print(f"Excluir Estoque: {estoque}")
        self.populate_table()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListarEstoqueWindow()
    window.show()
    sys.exit(app.exec())
