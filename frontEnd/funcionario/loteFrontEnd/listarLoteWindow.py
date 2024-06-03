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

from lote import Lote
from mensagemWindow import MensagemWindow
from .alterarLoteWindow import  AlterarLoteWindow


class ListarLoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listar lotes")
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
        self.lotes = Lote.listar_lote()
        self.table_widget.setRowCount(len(self.lotes))
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["LoteID", "Nome", "Data de produção", "Alterar", "Excluir"])

        for row, lote in enumerate(self.lotes):
            lote_id_item = QTableWidgetItem(f"{lote[0]}")
            self.table_widget.setItem(row, 0, lote_id_item)

            nome_item = QTableWidgetItem(f"{lote[2]}")
            self.table_widget.setItem(row, 1, nome_item)

            data_producao_item = QTableWidgetItem(lote[3].strftime("%d/%m/%Y"))
            self.table_widget.setItem(row, 2, data_producao_item)

            alterar_button = QPushButton("Alterar")
            alterar_button.clicked.connect(lambda _, l=lote: self.alterar_lote(l))
            self.table_widget.setCellWidget(row, 3, alterar_button)

            excluir_button = QPushButton("Excluir")
            excluir_button.clicked.connect(lambda _, l=lote: self.excluir_lote(l))
            self.table_widget.setCellWidget(row, 4, excluir_button)

    def alterar_lote(self, lote):
        self.selectedOption = AlterarLoteWindow(lote)
        self.selectedOption.window_closed.connect(self.populate_table)
        self.selectedOption.show()

        print(f"Alterar lote: {lote}")

    def excluir_lote(self, lote):
        Lote.excluir_lote(lote[0])
        self.msg = MensagemWindow(False,f"Lote de id {lote[0]} excluído com sucesso")
        self.msg.show()
        print(f"Excluir lote: {lote}")
        self.populate_table()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListarLoteWindow()
    window.show()
    sys.exit(app.exec())
