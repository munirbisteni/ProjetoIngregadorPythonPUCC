import sys

sys.path.append('./backEnd')
from receitaIngrediente import ReceitaIngredientes
from pedido import Pedido
from lote import Lote
from receita import Receita
from utilities import Utilities
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QComboBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem
)
from mensagemWindow import MensagemWindow

class CadastrarPedidoWindow(QMainWindow):
    def __init__(self, clienteID):
        super().__init__()
        self.clienteID = clienteID
        print(self.clienteID)
        self.vendaID = Pedido.cadastrar_venda(self.clienteID)
        print("vendaID:" + str(self.vendaID))

        self.setWindowTitle("Cadastrar Pedido")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()

        self.widgets = {
                    "cmb_pedido":QComboBox(),
                    "lbl_ingredientes": QLabel(),
                    "lbl_qtd":QLabel("Quantidade desejada:"),
                    "lbl_qtd":QSpinBox(),
                    "btn_cadastrarPedido":QPushButton("Cadastrar item"),
                    "tabela_pedido": QTableWidget(),
                    "lbl_valorTotal": QLabel(),
                    "btn_cadastrarVenda":QPushButton("Concluir")   
        }
        self.populate_table()
        self.widgets["cmb_pedido"].currentIndexChanged.connect(lambda index: self.listarIngredientes(self.widgets["cmb_pedido"].currentData()))

        receitasComValor = Receita.listar_receitasDisponiveis()
        self.widgets["cmb_pedido"].addItem(" - ", 0)
        for item in receitasComValor:
            self.widgets["cmb_pedido"].addItem(f"{item[2]} - Valor R$(UN):{item[1]}", item[0])

        self.widgets["btn_cadastrarPedido"].clicked.connect(self.btn_cadastrarPedidoClick)
        self.widgets["btn_cadastrarVenda"].clicked.connect(self.btn_cadastrarVendaClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def populate_table(self):
            self.itensPedido = Pedido.listar_pedidosVenda(self.vendaID)
            self.widgets["tabela_pedido"].setRowCount(len(self.itensPedido))
            self.widgets["tabela_pedido"].setColumnCount(5)
            self.widgets["tabela_pedido"].setHorizontalHeaderLabels(["Nome", "quantidade", "valor","Valor total do item" ,"Excluir"])
            for row, item in enumerate(self.itensPedido):
                nome_item = QTableWidgetItem(f"{item[3]}")
                self.widgets["tabela_pedido"].setItem(row, 0, nome_item)

                qtd_item = QTableWidgetItem(f"{item[2]}")
                self.widgets["tabela_pedido"].setItem(row, 1, qtd_item)

                qtd_item = QTableWidgetItem(f"{item[1]}")
                self.widgets["tabela_pedido"].setItem(row, 2, qtd_item)

                qtd_valorTotal = QTableWidgetItem(f"{float(item[2]) * float(item[1])}")
                self.widgets["tabela_pedido"].setItem(row, 3, qtd_valorTotal)

                excluir_button = QPushButton("Excluir")
                excluir_button.clicked.connect(lambda _, e=item: self.excluir(e))
                self.widgets["tabela_pedido"].setCellWidget(row, 4, excluir_button)

    def excluir(self, pedidoItem):
        Pedido.excluir_itemPedido(pedidoItem[0])
        self.msg = MensagemWindow(False,f"Pedido item de nome {pedidoItem[3]} excluído com sucesso")
        self.msg.show()
        print(f"Excluir ingrediente: {pedidoItem}")
        self.atualizar_lbl_valorTotal()
        self.populate_table()

    def atualizar_lbl_valorTotal(self):
        vendaAtual = Pedido.listar_vendaByID(self.vendaID)
        print(vendaAtual)
        self.widgets["lbl_valorTotal"].setText(f"Valor total: {vendaAtual[0][1]}")

    def listarIngredientes(self, receitaID):
        receitaIngredientes = ReceitaIngredientes.listar_receitaIngredientesByID(receitaID)
        formatado = ""
        for item in receitaIngredientes:
            formatado += f"{item[1]}, Usado: {item[2]} - {item[3]} | alergênico: {"sim" if item[4] == True else "Não"}\n"
        self.widgets["lbl_ingredientes"].setText(formatado)       

    def btn_cadastrarPedidoClick(self):
        dadosCadastrais = {
            "vendaID": self.vendaID,
            "cmb_pedido":  self.widgets["cmb_pedido"].currentData(),
            "lbl_qtd": self.widgets["lbl_qtd"].value()
        }        

        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False or dadosCadastrais["cmb_pedido"] == 0:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()

        else:
            self.widgets["lbl_qtd"].setValue(0)
            res = Pedido.cadastrar_pedidoItem(dadosCadastrais["vendaID"],dadosCadastrais["cmb_pedido"], dadosCadastrais["lbl_qtd"])
            if res == None:
                self.populate_table()
                self.msg = MensagemWindow(False,"Item adicionado!")
                self.atualizar_lbl_valorTotal()
                self.msg.show() 
            else:
                self.msg = MensagemWindow(True, str(res))
                self.msg.show()       
    
    def btn_cadastrarVendaClick(self):
        self.msg = MensagemWindow(False,"Cadastro concluído com sucesso!")
        self.msg.show()
        self.close()   
    