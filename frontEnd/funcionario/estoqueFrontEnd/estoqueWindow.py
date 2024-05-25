import sys

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
from .cadastrarEstoqueWindow import CadastrarEstoqueWindow
from .listarEstoqueWindow import ListarEstoqueWindow
class EstoqueWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Estoque")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        self.widgets = {
            "btn_visualizarEstoques":QPushButton("Visualizar Estoques"),
            "btn_cadastrarEstoque":QPushButton("Cadastrar Estoque")
        }

        for w in self.widgets.values():
            layout.addWidget(w)

        self.widgets["btn_visualizarEstoques"].clicked.connect(self.btn_visualizarEstoquesClick)
        self.widgets["btn_cadastrarEstoque"].clicked.connect(self.btn_cadastrarEstoqueClick)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn_visualizarEstoquesClick(self):
        self.selectedOption = ListarEstoqueWindow()
        self.selectedOption.show()
        
    def btn_cadastrarEstoqueClick(self):
        self.selectedOption = CadastrarEstoqueWindow()
        self.selectedOption.show()


