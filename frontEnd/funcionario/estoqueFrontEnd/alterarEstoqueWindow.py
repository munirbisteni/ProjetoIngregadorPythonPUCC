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
from PyQt6.QtCore import pyqtSignal

class AlterarEstoqueWindow(QMainWindow):
    window_closed = pyqtSignal()   

    def __init__(self,estoque):
        super().__init__()
        self.estoque = estoque
        self.setWindowTitle("Alterar Estoque")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "lbl_validade":QLabel("Data de validade:"),
                    "dt_validade": QDateEdit(),
                    "lbl_QuantidadeRestante":QLabel(f"Quantidade restante - [{self.estoque[6]}]:"),
                    "inp_QuantidadeRestante":QDoubleSpinBox(),
                    "btn_alterarEstoque":QPushButton("Alterar")   
                }
        self.widgets["inp_QuantidadeRestante"].setRange(0.0, 999.99)
        self.widgets["inp_QuantidadeRestante"].setMinimumWidth(self.widgets["inp_QuantidadeRestante"].fontMetrics().horizontalAdvance("999.99"))

        self.widgets["dt_validade"].setDate(self.estoque[4])
        self.widgets["inp_QuantidadeRestante"].setValue(self.estoque[3])

        self.widgets["dt_validade"].setCalendarPopup(True)
        

        self.widgets["btn_alterarEstoque"].clicked.connect(self.btn_alterarEstoqueClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   


    def btn_alterarEstoqueClick(self):

        dadosCadastrais = {
            "estoqueID": self.estoque[0],
            "dt_validade": self.widgets["dt_validade"].date(),
            "inp_QuantidadeRestante":"{:.2f}".format(self.widgets["inp_QuantidadeRestante"].value()),
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            res = Estoque.alterar_estoque(dadosCadastrais["estoqueID"],dadosCadastrais["dt_validade"],dadosCadastrais["inp_QuantidadeRestante"])
            if isinstance(res, (int, float)):
                self.close()
                self.msg = MensagemWindow(False,"Estoque cadastrado com sucesso!")
                self.msg.show()
            else:
                self.msg = MensagemWindow(True,"Dados preenchidos incorretamente")
                self.msg.show()
    
    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)