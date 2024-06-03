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

from mensagemWindow import MensagemWindow
from pedido import Pedido
class ListarMeusPedidosWindow(QMainWindow):

    def __init__(self, clienteID):
        super().__init__()
        self.clienteID = clienteID
        self.setWindowTitle("Listar meus pedidos")
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
        self.pedidos = Pedido.listar_vendasByUserID(self.clienteID)
        self.table_widget.setRowCount(len(self.pedidos))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Valor total", "itens", "status ", "Cancelar"])
        for row, pedido in enumerate(self.pedidos):
            receita_nome_item = QTableWidgetItem(f"{pedido[1]}")
            self.table_widget.setItem(row, 0, receita_nome_item)

            itensPedido = Pedido.listar_pedidosVenda(pedido[0])
            formatado = ""
            for item in itensPedido:
                formatado += f"{item[3]} - {item[2]} unidades\n"
            descricao = QTableWidgetItem(f"{formatado}")
            self.table_widget.setItem(row, 1, descricao)

            self.table_widget.resizeColumnToContents(1)            
            self.table_widget.resizeRowToContents(row)
            
            status = QTableWidgetItem(f"{pedido[2]}")
            self.table_widget.setItem(row, 2, status)

            if(pedido[3] == 8):
                excluir_button = QPushButton("Cancelar")
                excluir_button.clicked.connect(lambda _, e=pedido: self.cancelar(e))
                self.table_widget.setCellWidget(row, 3, excluir_button)
            else:
                impossivel_cancelar = QPushButton(f" - ")
                self.table_widget.setCellWidget(row, 3, impossivel_cancelar)

    def cancelar(self, pedido):
        Pedido.cancelar_venda(pedido[0])
        self.msg = MensagemWindow(False,f"pedido de id {pedido[0]} excluído com sucesso")
        self.msg.show()
        print(f"Cancelar pedido: {pedido}")
        self.populate_table()