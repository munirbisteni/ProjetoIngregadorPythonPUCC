# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QPushButton,
#     QTableWidget,
#     QTableWidgetItem,
#     QVBoxLayout,
#     QMainWindow,
#     QWidget,
# )

# from pedido import Pedido
# from mensagemWindow import MensagemWindow
# from .alterarPedidoWindow import AlterarPedidoWindow

# class ListarPedidosWindow(QMainWindow):
#     def _init_(self):
#         super()._init_()

#         self.setWindowTitle("Listar Pedidos")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.layout = QVBoxLayout()
#         self.table_widget = QTableWidget()
#         self.layout.addWidget(self.table_widget)

#         self.initUI()

#     def initUI(self):
#         self.populate_table()

#         widget = QWidget()
#         widget.setLayout(self.layout)
#         self.setCentralWidget(widget)
    
#     def populate_table(self):
#         self.pedidos = Pedido.listar_pedidos()
#         self.table_widget.setRowCount(len(self.pedidos))
#         self.table_widget.setColumnCount(5)
#         self.table_widget.setHorizontalHeaderLabels(["PedidoID", "Cliente", "Produto", "Data do Pedido", "Alterar", "Excluir"])

#         for row, pedido in enumerate(self.pedidos):
#             pedido_id_item = QTableWidgetItem(f"{pedido[0]}")
#             self.table_widget.setItem(row, 0, pedido_id_item)

#             cliente_item = QTableWidgetItem(f"{pedido[1]}")
#             self.table_widget.setItem(row, 1, cliente_item)

#             produto_item = QTableWidgetItem(f"{pedido[2]}")
#             self.table_widget.setItem(row, 2, produto_item)

#             data_pedido_item = QTableWidgetItem(pedido[3].strftime("%d/%m/%Y"))
#             self.table_widget.setItem(row, 3, data_pedido_item)

#             alterar_button = QPushButton("Alterar")
#             alterar_button.clicked.connect(lambda _, p=pedido: self.alterar_pedido(p))
#             self.table_widget.setCellWidget(row, 4, alterar_button)

#             excluir_button = QPushButton("Excluir")
#             excluir_button.clicked.connect(lambda _, p=pedido: self.excluir_pedido(p))
#             self.table_widget.setCellWidget(row, 5, excluir_button)

#     def alterar_pedido(self, pedido):
#         self.selectedOption = AlterarPedidoWindow(pedido)
#         self.selectedOption.window_closed.connect(self.populate_table)
#         self.selectedOption.show()

#         print(f"Alterar pedido: {pedido}")

#     def excluir_pedido(self, pedido):
#         Pedido.excluir_pedido(pedido[0])
#         self.msg = MensagemWindow(False, f"Pedido de id {pedido[0]} excluído com sucesso")
#         self.msg.show()
#         print(f"Excluir pedido: {pedido}")
#         self.populate_table()

# if _name_ == "_main_":
#     app = QApplication(sys.argv)
#     window = ListarPedidosWindow()
#     window.show()
#     sys.exit(app.exec())