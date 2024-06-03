import sys
sys.path.append('./backEnd')

from lote import Lote
from ingrediente import Ingrediente
from utilities import Utilities
from unidade import Unidade
from PyQt6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,   
    QCheckBox,
    QComboBox
)

from mensagemWindow import MensagemWindow
from PyQt6.QtCore import pyqtSignal

class AlterarIngredienteWindow(QMainWindow):
    window_closed = pyqtSignal()   
    
    def __init__(self, ingrediente):
        super().__init__()
        self.ingrediente = ingrediente
        self.setWindowTitle("Alterar ingredientes")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "inp_nome":QLineEdit(),
                    "chk_alergenico":QCheckBox("Alergênico"),
                    "cmb_unidade":QComboBox(),
                    "btn_cadastrarReceita":QPushButton("Continuar")   
                }
        self.widgets["inp_nome"].setPlaceholderText("Nome da receita")
        self.widgets["inp_nome"].setText(self.ingrediente[1])
        self.widgets["chk_alergenico"].setChecked(self.ingrediente[2])
        
        unidades = Unidade.listar_unidade()
        for index,item in enumerate(unidades):
            self.widgets["cmb_unidade"].addItem(item[2], item[0])
            if self.ingrediente[1] == item[0]:
                self.widgets["cmb_unidade"].setCurrentIndex(index)
        
        self.widgets["btn_cadastrarReceita"].clicked.connect(self.btn_alterarIngredienteClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def btn_alterarIngredienteClick(self):
        dadosCadastrais = {
            "ingredienteID": self.ingrediente[0],
            "inp_nome":  self.widgets["inp_nome"].text(),
            "cmb_unidade": self.widgets["cmb_unidade"].currentData()
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            Ingrediente.alterar_ingrediente(dadosCadastrais["inp_nome"],self.widgets["chk_alergenico"].isChecked(), dadosCadastrais["cmb_unidade"], dadosCadastrais["ingredienteID"])
            self.close()
            self.msg = MensagemWindow(False,"ingrediente alterado")
            self.msg.show()

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)