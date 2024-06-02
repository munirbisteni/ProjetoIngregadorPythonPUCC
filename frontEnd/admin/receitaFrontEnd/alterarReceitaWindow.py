import sys

sys.path.append('./backEnd')

from lote import Lote
from receita import Receita
from utilities import Utilities
from criptografia import Criptografia
from receitaIngrediente import ReceitaIngredientes
from PyQt6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,   
    QDoubleSpinBox,
    QLabel
)

from mensagemWindow import MensagemWindow
from .cadastrarReceitaIngredientesWindow import CadastrarReceitaIngredientesWindow
from PyQt6.QtCore import pyqtSignal

class AlterarReceitaWindow(QMainWindow):
    window_closed = pyqtSignal()   

    def __init__(self, receita):
        super().__init__()
        self.receita = receita
        self.setWindowTitle("Segunda Tela")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "inp_nome":QLineEdit(),
                    "inp_desc":QLineEdit(),
                    "lbl_ingredientes": QLabel(),
                    "lbl_valor": QLabel("Valor unitário de venda - 0 se não houver um lote produzido:"),
                    "qsp_valorVenda":QDoubleSpinBox(),
                    "btn_cadastrarReceita":QPushButton("Concluir alteração")
                }
        self.widgets["inp_nome"].setPlaceholderText("Nome da receita")
        self.widgets["inp_desc"].setPlaceholderText("Descrição da receita")
        self.widgets["inp_nome"].setText(receita[2])
        self.widgets["inp_desc"].setText(receita[3])
        self.widgets["qsp_valorVenda"].setValue(round(receita[1], 2))
        self.widgets["btn_cadastrarReceita"].clicked.connect(self.btn_AlterarReceitaClick)
        for w in self.widgets.values():
            self.layout.addWidget(w)
        self.lbl_ingredientesUsadosAtt()
        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def lbl_ingredientesUsadosAtt(self):
        receitaIngredientes = ReceitaIngredientes.listar_receitaIngredientesByID(self.receita[0])
        formatado = ""
        for item in receitaIngredientes:
            formatado += f"{item[1]}, Usado: {item[2]} - {item[3]}\n"
        self.widgets["lbl_ingredientes"].setText(formatado)

    def btn_AlterarReceitaClick(self):
        dadosCadastrais = {
            "receitaID": self.receita[0],
            "inp_nome":  self.widgets["inp_nome"].text(),
            "inp_desc": self.widgets["inp_desc"].text(),
            "inp_valorVenda": "{:.2f}".format(self.widgets["qsp_valorVenda"].value())
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            cripto = Criptografia()
            dadosCadastrais["inp_desc"] = cripto.criptografar(dadosCadastrais["inp_desc"])
            Receita.alterar_receita(dadosCadastrais["inp_nome"], dadosCadastrais["inp_desc"], dadosCadastrais["inp_valorVenda"], dadosCadastrais["receitaID"])
            self.msg = MensagemWindow(False,"Dados alterados")
            self.msg.show()
                
    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)