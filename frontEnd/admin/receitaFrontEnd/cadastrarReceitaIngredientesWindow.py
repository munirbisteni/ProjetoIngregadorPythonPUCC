import sys

sys.path.append('./backEnd')
from lote import Lote
from loteEstoque import LoteEstoque
from receita import Receita
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

class CadastrarReceitaIngredientesWindow(QMainWindow):
    def __init__(self, loteID,receitaID):
        super().__init__()
        self.loteID = loteID
        self.receitaID = receitaID
        
        self.setWindowTitle("Segunda Tela")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "cmb_estoque":QComboBox(),
                    "btn_novoLoteEstoque":QPushButton("Cadastrar este estoque como usado no lote"),   
                    "btn_concluir":QPushButton("Concluir")
                }
        
        estoque = Estoque.listar_estoque_by_receita(self.receitaID)

        if len(estoque) == 0:
            self.widgets["cmb_estoque"].addItem("Não há estoques para esse lote")
            self.widgets["btn_novoLoteEstoque"].clicked.connect(self.btn_erroClick)
            self.widgets["btn_concluir"].clicked.connect(self.btn_erroClick)

        else:
            self.widgets["cmb_estoque"].addItem(" - ", 0)
            for item in estoque:
                self.widgets["cmb_estoque"].addItem("Produto: "+ str(item[0] +" Data validade:" + item[5].strftime("%d/%m/%Y") + " EstoqueID: " + str(item[1])), item[1])

            self.widgets["btn_novoLoteEstoque"].clicked.connect(self.btn_novoLoteEstoqueClick)
            self.widgets["btn_concluir"].clicked.connect(self.btn_concluirCadastroClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def onDataProducaoClick(self):
         self.widgets["dt_vencimento"].setMinimunDate(self.widgets["dt_producao"].date())


    def btn_novoLoteEstoqueClick(self):

        dadosCadastrais = {
                "loteID": self.loteID,
                "cmb_estoque":  self.widgets["cmb_estoque"].currentData()
            }        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        
        else:
            res = LoteEstoque.cadastrar_loteEstoque(dadosCadastrais["loteID"],dadosCadastrais["cmb_estoque"])
            if res:
                self.msg = MensagemWindow(False,"Dado cadastrado com sucesso")
                self.msg.show()
            else:
                self.msg = MensagemWindow(True,"Dados preenchidos incorretamente")
                self.msg.show()
        
    def btn_erroClick(self):
        self.msg = MensagemWindow(True,"Este lote não será cadastrado por falta de ingredientes em estoque")
        self.msg.show()
        Lote.excluir_lote(self.loteID)
        self.close()    
    
    def btn_concluirCadastroClick(self):
        Lote.definir_CadastroConcluidoLote(self.loteID)
        self.msg = MensagemWindow(False,"Cadastro concluído com sucesso!")
        self.msg.show()
        self.close()    
        