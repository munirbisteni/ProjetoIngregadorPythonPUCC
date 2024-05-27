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
from .listarIngredientesWindow import ListarIngredienteWindow
from .cadastrarIngredienteWindow import CadastrarIngredienteWindow

class IngredienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ingrediente")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        self.widgets = {
            "btn_listar":QPushButton("Listar Ingredientes"),
            "btn_cadastrar":QPushButton("Cadastrar ingrediente"),
        }

        for w in self.widgets.values():
            layout.addWidget(w)
        self.widgets["btn_listar"].clicked.connect(self.btn_listarClick)
        self.widgets["btn_cadastrar"].clicked.connect(self.btn_cadastrarClick)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn_listarClick(self):
        self.selectedOption = ListarIngredienteWindow()
        self.selectedOption.show()

    def btn_cadastrarClick(self):
        self.selectedOption = CadastrarIngredienteWindow()
        self.selectedOption.show()
