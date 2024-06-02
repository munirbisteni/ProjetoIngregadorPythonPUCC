import sys

sys.path.append('./backEnd')
from lote import Lote
from loteEstoque import LoteEstoque
from receitaIngrediente import ReceitaIngredientes

from ingrediente import Ingrediente
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

class CadastrarReceitaIngredientesWindow(QMainWindow):
    def __init__(self, receitaID):
        super().__init__()
        self.receitaID = receitaID
        
        self.setWindowTitle("Cadastrar ingredientes da receita")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "cmb_ingredientes":QComboBox(),
                        "lbl_ingredientes":QLabel("Os ingredientes usados aparecerão aqui"),
                    "lbl_qtdUsada":QLabel(f"Quantidade usada:"),
                    "intp_qtdUsada":QDoubleSpinBox(),
                    "btn_cadastrarIngrediente":QPushButton("Cadastrar este ingrediente"),   
                    "btn_concluir":QPushButton("Concluir")
                }
        
        ingredientes = Ingrediente.listar_ingredientes()
        
        self.widgets["intp_qtdUsada"].setRange(0.0, 999.99)
        self.widgets["intp_qtdUsada"].setMinimumWidth(self.widgets["intp_qtdUsada"].fontMetrics().horizontalAdvance("999.99"))
        
        self.widgets["cmb_ingredientes"].addItem(" - ", 0)
        for item in ingredientes:
            self.widgets["cmb_ingredientes"].addItem(f"{item[1]} - medida: {item[3]}", item[0])

        self.widgets["btn_cadastrarIngrediente"].clicked.connect(self.btn_cadastrarIngredienteClick)
        self.widgets["btn_concluir"].clicked.connect(self.btn_concluirCadastroClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def lbl_ingredientesUsadosAtt(self):
        receitaIngredientes = ReceitaIngredientes.listar_receitaIngredientesByID(self.receitaID)
        formatado = ""
        for item in receitaIngredientes:
            formatado += f"{item[1]}, Usado: {item[2]} - {item[3]}\n"
        self.widgets["lbl_ingredientes"].setText(formatado)

         
    def btn_cadastrarIngredienteClick(self):

        dadosCadastrais = {
                "receitaID": self.receitaID,
                "cmb_ingredientes": self.widgets["cmb_ingredientes"].currentData(),
                "intp_qtdUsada": "{:.2f}".format(self.widgets["intp_qtdUsada"].value()),
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            ReceitaIngredientes.cadastrar_receitaIngredientes(dadosCadastrais["receitaID"],dadosCadastrais["cmb_ingredientes"], dadosCadastrais["intp_qtdUsada"])
            self.msg = MensagemWindow(False,"Dado cadastrado com sucesso")
            self.lbl_ingredientesUsadosAtt()
            self.msg.show()


    def btn_concluirCadastroClick(self):
        self.msg = MensagemWindow(False,"Cadastro concluído com sucesso!")
        self.msg.show()
        self.close()    
        