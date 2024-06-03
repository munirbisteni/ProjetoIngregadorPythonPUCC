import sys
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QComboBox
)

from mensagemWindow import MensagemWindow
from pedido import Pedido
class ListarPedidosWindow(QMainWindow):

    def __init__(self):
        super().__init__()
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
        self.pedidos = Pedido.listar_vendas()
        self.statusVenda = Pedido.listar_statusVenda()
        print(self.statusVenda)
        cmb_status = QComboBox()
        self.table_widget.setRowCount(len(self.pedidos))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Valor total", "itens", "status "])
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

            cmb_status = QComboBox()
            for index, item in enumerate(self.statusVenda):
                cmb_status.addItem(item[1], item[0])
                if item[0] == pedido[3]:
                    cmb_status.setCurrentIndex(index)
            cmb_status.currentIndexChanged.connect(lambda index, cmb=cmb_status: self.alterar_status(cmb.currentData(), pedido[0]))
            self.table_widget.setCellWidget(row, 2, cmb_status)

    def alterar_status(self, statusID, vendaID):
        Pedido.alterar_status(vendaID, statusID)
        self.msg = MensagemWindow(False,f"pedido de id {vendaID} alterado para o status de ID {statusID} com sucesso")
        self.msg.show()
        print(f"alterar pedido: {vendaID}")
