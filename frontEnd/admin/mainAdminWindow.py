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
from admin.usuarioFrontEnd.usuarioWindow import UsuarioWindow
from admin.receitaFrontEnd.receitaWindow import ReceitaWindow
from admin.ingredienteFrontEnd.ingredienteWindow import IngredienteWindow
from admin.custosGeraisWindow import CustosGeraisWindow
class MainAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Administrador")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        self.widgets = {
            "btn_usuario":QPushButton("Usuários"),
            "btn_receita":QPushButton("Receitas"),
            "btn_ingrediente":QPushButton("Ingredientes"),
            "btn_custosGerais":QPushButton("Custos Gerais")     
 
        }

        for w in self.widgets.values():
            layout.addWidget(w)
        self.widgets["btn_usuario"].clicked.connect(self.btn_usuarioClick)
        self.widgets["btn_receita"].clicked.connect(self.btn_receitaClick)
        self.widgets["btn_ingrediente"].clicked.connect(self.btn_ingredienteClick)
        self.widgets["btn_custosGerais"].clicked.connect(self.btn_custosGeraisClick)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn_usuarioClick(self):
        self.selectedOption = UsuarioWindow()
        self.selectedOption.show()

    def btn_receitaClick(self):
        self.selectedOption = ReceitaWindow()
        self.selectedOption.show()

    def btn_ingredienteClick(self):
        self.selectedOption = IngredienteWindow()
        self.selectedOption.show()

    def btn_custosGeraisClick(self):
        self.selectedOption = CustosGeraisWindow()
        self.selectedOption.show()