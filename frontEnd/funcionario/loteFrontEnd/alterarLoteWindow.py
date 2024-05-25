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
from PyQt6.QtCore import pyqtSignal

class AlterarLoteWindow(QMainWindow):
    window_closed = pyqtSignal()   
    def __init__(self, lote):
        super().__init__()
        self.lote = lote
        self.setWindowTitle("Segunda Tela")
        self.setGeometry(100, 100, 400, 200)
        
       
        self.layout = QVBoxLayout()
        self.widgets = {
                    "cmb_receita":QComboBox(),
                    "lbl_producao":QLabel("Data de produção:"),
                    "dt_producao": QDateEdit(),
                    "lbl_vencimento":QLabel("Data de vencimento:"),
                    "dt_vencimento": QDateEdit(),
                    "lbl_qtdRestante":QLabel("Quantidade restante:"),
                    "inp_qtdRestante":QSpinBox(),
                    "btn_cadastrarLoteEstoque":QPushButton("Continuar")   
                }
        self.widgets["dt_producao"].setCalendarPopup(True)
        self.widgets["dt_producao"].setDate(self.lote[3])
        self.widgets["dt_vencimento"].setDate(self.lote[4])
        self.widgets["dt_vencimento"].setCalendarPopup(True)
        self.widgets["inp_qtdRestante"].setValue(self.lote[7])

        receitas = Receita.listar_receitas()
        for index, item in enumerate(receitas):
            self.widgets["cmb_receita"].addItem(item[2], item[0])
            if self.lote[1] == item[0]:
                self.widgets["cmb_receita"].setCurrentIndex(index)

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
            "loteID": self.lote[0],
            "cmb_receita":  self.widgets["cmb_receita"].currentData(),
            "dt_producao": self.widgets["dt_producao"].date(),
            "dt_vencimento": self.widgets["dt_vencimento"].date(),
            "inp_qtdRestante":self.widgets["inp_qtdRestante"].text()
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            res = Lote.atualizar_lote(dadosCadastrais["loteID"],dadosCadastrais["cmb_receita"],dadosCadastrais["dt_producao"], dadosCadastrais["dt_vencimento"], dadosCadastrais["inp_qtdRestante"])
            if res:
                self.msg = MensagemWindow(False,"Dados alterados com sucesso")
                self.msg.show()
                self.close()
            else:
                self.msg = MensagemWindow(True,"Dados preenchidos incorretamente")
                self.msg.show()


    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)