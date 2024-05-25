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
from .cadastrarLoteWindow import CadastrarLoteWindow
from .listarLoteWindow import ListarLoteWindow
class LoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lote")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        self.widgets = {
            "btn_visualizarLotes":QPushButton("Visualizar lotes"),
            "btn_cadastrarLote":QPushButton("Cadastrar lote")     
        }

        for w in self.widgets.values():
            layout.addWidget(w)

        self.widgets["btn_visualizarLotes"].clicked.connect(self.btn_visualizarLotesClick)
        self.widgets["btn_cadastrarLote"].clicked.connect(self.btn_cadastrarLoteClick)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn_visualizarLotesClick(self):
        self.selectedOption = ListarLoteWindow()
        self.selectedOption.show()
        
    def btn_cadastrarLoteClick(self):
        self.selectedOption = CadastrarLoteWindow()
        self.selectedOption.show()