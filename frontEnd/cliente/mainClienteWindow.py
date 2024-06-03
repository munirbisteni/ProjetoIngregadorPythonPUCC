import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QGridLayout
)
from cliente.listarMeusPedidosWindow import ListarMeusPedidosWindow
from cliente.cadastrarPedidoWindow import CadastrarPedidoWindow
class ClienteWindow(QMainWindow):
    def __init__(self, clienteID):
        super().__init__()
        self.clienteID = clienteID
        self.setWindowTitle("área do cliente")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        self.widgets = {
            "btn_novoPedido":QPushButton("Realizar pedido"),
            "btn_listarPedidos":QPushButton("Ver meus pedidos")     
        }

        for w in self.widgets.values():
            layout.addWidget(w)
        self.widgets["btn_novoPedido"].clicked.connect(self.btn_novoPedidoClick)
        self.widgets["btn_listarPedidos"].clicked.connect(self.btn_listarPedidosClick)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn_novoPedidoClick(self):
        self.selectedOption = CadastrarPedidoWindow(self.clienteID)
        self.selectedOption.show()

    def btn_listarPedidosClick(self):
        self.selectedOption = ListarMeusPedidosWindow(self.clienteID)
        self.selectedOption.show()