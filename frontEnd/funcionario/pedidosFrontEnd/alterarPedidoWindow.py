# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QComboBox,
#     QLabel,
#     QDateEdit,
#     QSpinBox,
#     QPushButton,
#     QVBoxLayout,
#     QMainWindow,
#     QWidget,
# )
# from PyQt6.QtCore import QDate, pyqtSignal
# from pedido import Pedido
# from cliente import Cliente
# from produto import Produto
# from mensagemWindow import MensagemWindow
# from utilities import Utilities

# class AlterarPedidoWindow(QMainWindow):
#     window_closed = pyqtSignal()

#     def _init_(self, pedido):
#         super()._init_()
#         self.pedido = pedido
#         self.setWindowTitle("Alterar Pedido")
#         self.setGeometry(100, 100, 400, 300)

#         self.layout = QVBoxLayout()
#         self.widgets = {
#             "cmb_cliente": QComboBox(),
#             "cmb_produto": QComboBox(),
#             "lbl_dataPedido": QLabel("Data do Pedido:"),
#             "dt_dataPedido": QDateEdit(),
#             "lbl_qtdProduto": QLabel("Quantidade do Produto:"),
#             "inp_qtdProduto": QSpinBox(),
#             "btn_alterarPedido": QPushButton("Alterar Pedido")
#         }

#         # Populando combobox de clientes
#         clientes = Cliente.listar_clientes()
#         for index, item in enumerate(clientes):
#             self.widgets["cmb_cliente"].addItem(item[1], item[0])
#             if self.pedido[1] == item[0]:
#                 self.widgets["cmb_cliente"].setCurrentIndex(index)

#         # Populando combobox de produtos
#         produtos = Produto.listar_produtos()
#         for index, item in enumerate(produtos):
#             self.widgets["cmb_produto"].addItem(item[1], item[0])
#             if self.pedido[2] == item[0]:
#                 self.widgets["cmb_produto"].setCurrentIndex(index)

#         self.widgets["dt_dataPedido"].setCalendarPopup(True)
#         self.widgets["dt_dataPedido"].setDate(self.pedido[3])

#         self.widgets["inp_qtdProduto"].setValue(self.pedido[4])

#         self.widgets["btn_alterarPedido"].clicked.connect(self.btn_alterarPedidoClick)

#         for w in self.widgets.values():
#             self.layout.addWidget(w)

#         widget = QWidget()
#         widget.setLayout(self.layout)
#         self.setCentralWidget(widget)

#     def btn_alterarPedidoClick(self):
#         dadosCadastrais = {
#             "pedidoID": self.pedido[0],
#             "clienteID": self.widgets["cmb_cliente"].currentData(),
#             "produtoID": self.widgets["cmb_produto"].currentData(),
#             "dataPedido": self.widgets["dt_dataPedido"].date(),
#             "qtdProduto": self.widgets["inp_qtdProduto"].value()
#         }

#         flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
#         if not flagPreenchido:
#             self.msg = MensagemWindow(True, "Preencha todos os campos primeiramente")
#             self.msg.show()
#         else:
#             res = Pedido.atualizar_pedido(
#                 dadosCadastrais["pedidoID"],
#                 dadosCadastrais["clienteID"],
#                 dadosCadastrais["produtoID"],
#                 dadosCadastrais["dataPedido"],
#                 dadosCadastrais["qtdProduto"]
#             )
#             if res:
#                 self.msg = MensagemWindow(False, "Pedido alterado com sucesso")
#                 self.msg.show()
#                 self.close()
#             else:
#                 self.msg = MensagemWindow(True, "Dados preenchidos incorretamente")
#                 self.msg.show()

#     def closeEvent(self, event):
#         self.window_closed.emit()
#         super().closeEvent(event)

