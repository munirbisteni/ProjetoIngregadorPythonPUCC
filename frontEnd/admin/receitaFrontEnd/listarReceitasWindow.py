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
from receita import Receita
from .alterarReceitaWindow import AlterarReceitaWindow
from mensagemWindow import MensagemWindow

class ListarReceitasWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listar receitas")
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
        self.receitas = Receita.listar_receitas()
        self.table_widget.setRowCount(len(self.receitas))
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["Nome", "Valor de venda", "Descricao","Alterar", "Excluir"])
        for row, receita in enumerate(self.receitas):
            receita_nome_item = QTableWidgetItem(f"{receita[2]}")
            self.table_widget.setItem(row, 0, receita_nome_item)

            valor_venda_item = QTableWidgetItem(f"{receita[1]}")
            self.table_widget.setItem(row, 1, valor_venda_item)

            descricao = QTableWidgetItem(f"{receita[3]}")
            self.table_widget.setItem(row, 2, descricao)

            alterar_button = QPushButton("Alterar")
            alterar_button.clicked.connect(lambda _, e=receita: self.alterar(e))
            self.table_widget.setCellWidget(row, 3, alterar_button)

            excluir_button = QPushButton("Excluir")
            excluir_button.clicked.connect(lambda _, e=receita: self.excluir(e))
            self.table_widget.setCellWidget(row, 4, excluir_button)

    def alterar(self, receita):
        self.selectedOption = AlterarReceitaWindow(receita)
        self.selectedOption.window_closed.connect(self.populate_table)
        self.selectedOption.show()
        print(f"Alterar Estoque: {receita}")

    def excluir(self, receita):
        Receita.excluir_receita(receita[0])
        self.msg = MensagemWindow(False,f"receita de id {receita[0]} excluído com sucesso")
        self.msg.show()
        print(f"Excluir receita: {receita}")
        self.populate_table()