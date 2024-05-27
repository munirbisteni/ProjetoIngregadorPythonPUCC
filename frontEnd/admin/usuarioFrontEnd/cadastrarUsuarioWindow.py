import sys

sys.path.append('./backEnd')

from usuario import Usuario
from estado import Estado
from cidade import Cidade
from utilities import Utilities
from usuarioRoles import UsuarioRoles
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
from criptografia import Criptografia   

class CadastrarUsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segunda Tela")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "cmb_role":QComboBox(),
                    "inp_nome": QLineEdit(),
                    "inp_email":QLineEdit(),
                    "inp_senha":QLineEdit(),
                    "cmb_estado":QComboBox(),
                    "cmb_cidade":QComboBox(),
                    "inp_endereco":QLineEdit(),
                    "btn_registrar":QPushButton("Registrar")   
                }
        
        usuarioRoles = UsuarioRoles.listar_usuarioRoles()
        for item in usuarioRoles:
            self.widgets["cmb_role"].addItem(item[1], item[0])

        self.widgets["cmb_cidade"].setVisible(False)
        self.widgets["inp_email"].setPlaceholderText("Email")

        self.widgets["inp_senha"].setPlaceholderText("Senha")
        self.widgets["inp_senha"].setEchoMode(QLineEdit.EchoMode.Password)
        self.widgets["inp_nome"].setPlaceholderText("Nome")
        self.widgets["inp_endereco"].setPlaceholderText("Endereço")
        estados = Estado.listar_estados()
        self.widgets["cmb_estado"].addItem(" - ", 0)
        for item in estados:
            self.widgets["cmb_estado"].addItem(item[2], item[0])
        self.widgets["cmb_estado"].currentIndexChanged.connect(lambda index: self.estado_selecionado(self.widgets["cmb_estado"].currentData()))
        self.widgets["btn_registrar"].clicked.connect(self.btn_registrarClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   

    def estado_selecionado(self, estado_selecionado):
        cidades = Cidade.get_cidade_by_EstadoID(estado_selecionado)
        for item in cidades:
            self.widgets["cmb_cidade"].addItem(item[1], item[0])
        self.widgets["cmb_cidade"].setVisible(True)

    def btn_registrarClick(self):
        cripto = Criptografia()
        dadosCadastrais = {
            "role": self.widgets["cmb_role"].currentData(),
            "nome":  self.widgets["inp_nome"].text(),
            "email": self.widgets["inp_email"].text(),
            "senha": cripto.criptografar(self.widgets["inp_senha"].text()),
            "endereco": self.widgets["inp_endereco"].text(),
            "cidade":self.widgets["cmb_cidade"].currentData()
            }
        
        flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
        if flagPreenchido == False:
                self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                self.msg.show()
        else:
            Usuario.cadastrar_usuario(dadosCadastrais["role"],dadosCadastrais["nome"],dadosCadastrais["email"], dadosCadastrais["senha"], dadosCadastrais["endereco"],dadosCadastrais["cidade"])
            self.close()
            self.msg = MensagemWindow(False,"Dados cadastrados")
            self.msg.show()
            