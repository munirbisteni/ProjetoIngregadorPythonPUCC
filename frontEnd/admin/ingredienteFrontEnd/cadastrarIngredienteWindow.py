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

class CadastrarIngredienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segunda Tela")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "inp_nome":QLineEdit(),
                    "chk_alergenico":QCheckBox("Alergênico"),
                    "cmb_unidade":QComboBox(),
                    "btn_cadastrarReceita":QPushButton("Continuar")   
                }
        self.widgets["inp_nome"].setPlaceholderText("Nome da receita")
        unidades = Unidade.listar_unidade()
        for item in unidades:
             self.widgets["cmb_unidade"].addItem(item[2], item[0])
        self.widgets["btn_cadastrarReceita"].clicked.connect(self.btn_cadastrarIngredienteClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout) 
        self.setCentralWidget(widget)   

    def btn_cadastrarIngredienteClick(self):
        dadosCadastrais = {
            "inp_nome":  self.widgets["inp_nome"].text(),
            "cmb_unidade": self.widgets["cmb_unidade"].currentData()
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            Ingrediente.cadastrar_ingrediente(dadosCadastrais["inp_nome"],self.widgets["chk_alergenico"].isChecked(), dadosCadastrais["cmb_unidade"])
            self.close()
            self.msg = MensagemWindow(False,"ingrediente cadastrado")
            self.msg.show()