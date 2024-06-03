import sys

sys.path.append('./backEnd')

from usuario import Usuario
from estado import Estado
from cidade import Cidade
from utilities import Utilities
from usuarioRoles import UsuarioRoles
from custosGerais import CustosGerais
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QDate
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
)
from mensagemWindow import MensagemWindow

class CustosGeraisWindow(QMainWindow):

    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("Custos gerais")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "lbl_margem":QLabel("Margem de lucro (em porcentagem):"),
                    "inp_margem": QDoubleSpinBox(),
                    "lbl_margem_idf":QLabel(),

                    "lbl_custoFixo":QLabel("Custo fixo (em porcentagem):"),
                    "inp_custoFixo":QDoubleSpinBox(),
                    
                    "lbl_imposto":QLabel("Imposto (em porcentagem):"),
                    "inp_imposto":QDoubleSpinBox(),
                    
                    "btn_alterar":QPushButton("Alterar")   
                }
        self.widgets["inp_margem"].setRange(0.0, 999.99)
        self.widgets["inp_margem"].setMinimumWidth( self.widgets["inp_margem"].fontMetrics().horizontalAdvance("999.99"))
        
        self.widgets["inp_custoFixo"].setRange(0.0, 999.99)
        self.widgets["inp_custoFixo"].setMinimumWidth( self.widgets["inp_custoFixo"].fontMetrics().horizontalAdvance("999.99"))
        
        self.widgets["inp_imposto"].setRange(0.0, 999.99)
        self.widgets["inp_imposto"].setMinimumWidth( self.widgets["inp_imposto"].fontMetrics().horizontalAdvance("999.99"))
        custos = CustosGerais.listar_custosGerais()
        for item in custos:
             if(item[3] == "ML"):
                self.widgets["inp_margem"].setValue(item[2])
                self.definirLucro(item[2])
             if(item[3] == "CF"):
                self.widgets["inp_custoFixo"].setValue(item[2])
             if(item[3] == "IMPOSTO"):
                self.widgets["inp_imposto"].setValue(item[2])   

        self.widgets["btn_alterar"].clicked.connect(self.btn_alterarClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def definirLucro(self, ML):
        if ML > 20:
            self.widgets["lbl_margem_idf"].setStyleSheet("color: blue") 
            self.widgets["lbl_margem_idf"].setText("Lucro ALTO")
        elif ML > 10:
            self.widgets["lbl_margem_idf"].setStyleSheet("color: green") 
            self.widgets["lbl_margem_idf"].setText("Lucro MÉDIO")
        elif ML > 0:
            self.widgets["lbl_margem_idf"].setStyleSheet("color: yellow") 
            self.widgets["lbl_margem_idf"].setText("Lucro BAIXO")
        else:
            self.widgets["lbl_margem_idf"].setStyleSheet("color: red") 
            self.widgets["lbl_margem_idf"].setText("Prejuízo")         
    def btn_alterarClick(self):
            dadosCadastrais = {
                "inp_margem":  "{:.2f}".format(self.widgets["inp_margem"].value()),
                "inp_custoFixo": "{:.2f}".format(self.widgets["inp_custoFixo"].value()),
                "inp_imposto": "{:.2f}".format(self.widgets["inp_imposto"].value()),
            }
            flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
            if flagPreenchido == False or dadosCadastrais["inp_margem"] == 0.0 or dadosCadastrais["inp_custoFixo"] == 0.0 or dadosCadastrais["inp_imposto"] == 0:
                    self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                    self.msg.show()
            else:
                CustosGerais.alterar_custos_gerais(dadosCadastrais["inp_margem"],dadosCadastrais["inp_custoFixo"],dadosCadastrais["inp_imposto"])
                self.definirLucro(float(dadosCadastrais["inp_margem"]))
                self.msg = MensagemWindow(False,"Dados cadastrados")
                self.msg.show()
                self.close()
      