import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import (

    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from funcionario.loteFrontEnd.loteWindow import LoteWindow
from funcionario.estoqueFrontEnd.estoqueWindow import EstoqueWindow
from funcionario.pedidosFrontEnd.listarPedidosWindow import ListarPedidosWindow
class MainFuncionarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Funcionário")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        self.widgets = {
            "btn_estoque":QPushButton("Estoque"),
            "btn_lote":QPushButton("Lote"),
            "btn_pedido":QPushButton("Pedidos")     

        }

        for w in self.widgets.values():
            layout.addWidget(w)
        self.widgets["btn_estoque"].clicked.connect(self.btn_estoqueClick)
        self.widgets["btn_lote"].clicked.connect(self.btn_loteClick)
        self.widgets["btn_pedido"].clicked.connect(self.btn_pedidoClick)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn_estoqueClick(self):
        self.selectedOption = EstoqueWindow()
        self.selectedOption.show()

    def btn_loteClick(self):
        self.selectedOption = LoteWindow()
        self.selectedOption.show()

    def btn_pedidoClick(self):
        self.selectedOption = ListarPedidosWindow()
        self.selectedOption.show()
        return