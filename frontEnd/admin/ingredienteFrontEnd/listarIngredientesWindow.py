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

from ingrediente import Ingrediente
from .alterarIngredienteWindow import AlterarIngredienteWindow
from mensagemWindow import MensagemWindow

class ListarIngredientesWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listar Ingredientes")
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
        self.ingredientes = Ingrediente.listar_ingredientes()
        self.table_widget.setRowCount(len(self.ingredientes))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Nome", "medida" ,"Alterar", "Excluir"])
        for row, ingrediente in enumerate(self.ingredientes):
            nome_item = QTableWidgetItem(f"{ingrediente[1]}")
            self.table_widget.setItem(row, 0, nome_item)

            medida_item = QTableWidgetItem(f"{ingrediente[3]}")
            self.table_widget.setItem(row, 1, medida_item)

            alterar_button = QPushButton("Alterar")
            alterar_button.clicked.connect(lambda _, e=ingrediente: self.alterar(e))
            self.table_widget.setCellWidget(row, 2, alterar_button)

            excluir_button = QPushButton("Excluir")
            excluir_button.clicked.connect(lambda _, e=ingrediente: self.excluir(e))
            self.table_widget.setCellWidget(row, 3, excluir_button)

    def alterar(self, ingrediente):
        self.selectedOption = AlterarIngredienteWindow(ingrediente)
        self.selectedOption.window_closed.connect(self.populate_table)
        self.selectedOption.show()
        print(f"Alterar ingrediente: {ingrediente}")

    def excluir(self, ingrediente):
        Ingrediente.excluir_ingrediente(ingrediente[0])
        self.msg = MensagemWindow(False,f"ingrediente de id {ingrediente[0]} excluído com sucesso")
        self.msg.show()
        print(f"Excluir ingrediente: {ingrediente}")
        self.populate_table()