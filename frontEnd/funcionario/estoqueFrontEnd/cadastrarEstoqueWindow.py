import sys

sys.path.append('./backEnd')


from lote import Lote
from ingrediente import Ingrediente
from estoque import Estoque
from utilities import Utilities
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

class CadastrarEstoqueWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastrar Estoque")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "cmb_ingredientes":QComboBox(),
                    "lbl_validade":QLabel("Data de validade:"),
                    "dt_validade": QDateEdit(),
                    "lbl_quantidadeComprada":QLabel(f"Quantidade comprada:"),
                    "inp_quantidadeComprada":QDoubleSpinBox(), 
                    "lbl_valorCompra":QLabel("Valor pago:"),
                    "inp_valorCompra":QDoubleSpinBox(),
                    "btn_cadastrarEstoque":QPushButton("Cadastrar")   
                }
        self.widgets["inp_quantidadeComprada"].setRange(0.0, 9999.99)
        self.widgets["inp_quantidadeComprada"].setMinimumWidth( self.widgets["inp_quantidadeComprada"].fontMetrics().horizontalAdvance("999.99"))

        self.widgets["inp_valorCompra"].setRange(0.0, 9999.99)
        self.widgets["inp_valorCompra"].setMinimumWidth( self.widgets["inp_valorCompra"].fontMetrics().horizontalAdvance("999.99"))

        self.widgets["dt_validade"].setCalendarPopup(True)
        self.widgets["dt_validade"].setDate(QDate.currentDate())

        ingredientes = Ingrediente.listar_ingredientes()
        self.widgets["cmb_ingredientes"].addItem(" - ", 0)
        for item in ingredientes:
            self.widgets["cmb_ingredientes"].addItem(f"{item[1]} - [{item[3]}]", item[0])

        self.widgets["btn_cadastrarEstoque"].clicked.connect(self.btn_cadastrarEstoqueClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   


    def btn_cadastrarEstoqueClick(self):

        dadosCadastrais = {
            "cmb_ingredientes":  self.widgets["cmb_ingredientes"].currentData(),
            "dt_validade": self.widgets["dt_validade"].date(),
            "inp_quantidadeComprada":"{:.2f}".format(self.widgets["inp_quantidadeComprada"].value()),
            "inp_valorCompra":"{:.2f}".format(self.widgets["inp_valorCompra"].value())
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            res = Estoque.cadastrar_estoque(dadosCadastrais["cmb_ingredientes"],dadosCadastrais["dt_validade"], dadosCadastrais["inp_quantidadeComprada"], dadosCadastrais["inp_valorCompra"])
            if isinstance(res, (int, float)):
                self.close()
                self.msg = MensagemWindow(False,"Estoque cadastrado com sucesso!")
                self.msg.show()
            else:
                self.msg = MensagemWindow(True,"Dados preenchidos incorretamente")
                self.msg.show()
        