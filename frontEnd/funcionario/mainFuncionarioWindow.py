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
from funcionario.loteFrontEnd.loteWindow import LoteWindow
from funcionario.estoqueFrontEnd.estoqueWindow import EstoqueWindow

class MainFuncionarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Funcionário")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        self.widgets = {
            "btn_estoque":QPushButton("Estoque"),
            "btn_lote":QPushButton("Lote")     
        }

        for w in self.widgets.values():
            layout.addWidget(w)
        self.widgets["btn_estoque"].clicked.connect(self.btn_estoqueClick)
        self.widgets["btn_lote"].clicked.connect(self.btn_loteClick)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn_estoqueClick(self):
        self.selectedOption = EstoqueWindow()
        self.selectedOption.show()

    def btn_loteClick(self):
        self.selectedOption = LoteWindow()
        self.selectedOption.show()