import sys

sys.path.append('./backEnd')


from lote import Lote
from receita import Receita
from utilities import Utilities
from criptografia import Criptografia
from PyQt6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,   
)
from mensagemWindow import MensagemWindow
from .cadastrarReceitaIngredientesWindow import CadastrarReceitaIngredientesWindow

class CadastrarReceitaWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastrar receita")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "inp_nome":QLineEdit(),
                    "inp_desc":QLineEdit(),
                    "btn_cadastrarReceita":QPushButton("Continuar")   
                }
        self.widgets["inp_nome"].setPlaceholderText("Nome da receita")
        self.widgets["inp_desc"].setPlaceholderText("Descrição da receita")

        self.widgets["btn_cadastrarReceita"].clicked.connect(self.btn_cadastrarReceitaClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def btn_cadastrarReceitaClick(self):
        dadosCadastrais = {
            "inp_nome":  self.widgets["inp_nome"].text(),
            "inp_desc": self.widgets["inp_desc"].text()
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            cripto = Criptografia()
            dadosCadastrais["inp_desc"] = cripto.criptografar(dadosCadastrais["inp_desc"])
            res = Receita.cadastrar_receita(dadosCadastrais["inp_nome"], dadosCadastrais["inp_desc"])
            if isinstance(res, (int, float)):
                self.close()
                self.selectedOption = CadastrarReceitaIngredientesWindow(res)
                self.selectedOption.show()      
            else:
                self.msg = MensagemWindow(True,"Dados preenchidos incorretamente")
                self.msg.show()
        