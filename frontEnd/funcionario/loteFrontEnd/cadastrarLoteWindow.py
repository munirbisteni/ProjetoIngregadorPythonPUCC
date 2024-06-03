import sys

sys.path.append('./backEnd')


from lote import Lote
from receita import Receita
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
from .cadastrarLoteEstoqueWindow import CadastrarLoteEstoqueWindow

class CadastrarLoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastrar Lote")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "cmb_receita":QComboBox(),
                    "lbl_producao":QLabel("Data de produção:"),
                    "dt_producao": QDateEdit(),
                    "lbl_vencimento":QLabel("Data de vencimento:"),
                    "dt_vencimento": QDateEdit(),
                    "lbl_qtdProduzida":QLabel("Quantidade produzida:"),
                    "inp_qtdproduzida":QSpinBox(),
                    "btn_cadastrarLoteEstoque":QPushButton("Continuar")   
                }
        self.widgets["dt_producao"].setCalendarPopup(True)
        self.widgets["dt_producao"].setDate(QDate.currentDate())
        self.widgets["dt_producao"].setMaximumDate(QDate.currentDate())
        self.widgets["dt_producao"].dateChanged.connect(self.onDataProducaoClick)

        self.widgets["dt_vencimento"].setCalendarPopup(True)
        self.widgets["dt_vencimento"].setDate(QDate.currentDate())
        receitas = Receita.listar_receitas()
        self.widgets["cmb_receita"].addItem(" - ", 0)
        for item in receitas:
            self.widgets["cmb_receita"].addItem(item[2], item[0])

        self.widgets["btn_cadastrarLoteEstoque"].clicked.connect(self.btn_cadastrarLoteEstoqueClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def onDataProducaoClick(self):
         self.widgets["dt_vencimento"].setMinimunDate(self.widgets["dt_producao"].date())


    def btn_cadastrarLoteEstoqueClick(self):

        dadosCadastrais = {
            "cmb_receita":  self.widgets["cmb_receita"].currentData(),
            "dt_producao": self.widgets["dt_producao"].date(),
            "dt_vencimento": self.widgets["dt_vencimento"].date(),
            "inp_qtdproduzida":self.widgets["inp_qtdproduzida"].text()
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            res = Lote.cadastrar_lote(dadosCadastrais["cmb_receita"],dadosCadastrais["dt_producao"], dadosCadastrais["dt_vencimento"], dadosCadastrais["inp_qtdproduzida"])
            if isinstance(res, (int, float)):
                self.close()
                self.selectedOption = CadastrarLoteEstoqueWindow(res, dadosCadastrais["cmb_receita"])
                self.selectedOption.show()      
            else:
                self.msg = MensagemWindow(True,"Dados preenchidos incorretamente")
                self.msg.show()
        