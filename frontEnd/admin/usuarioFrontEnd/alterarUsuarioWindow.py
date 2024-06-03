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
from PyQt6.QtCore import pyqtSignal

class AlterarUsuarioWindow(QMainWindow):
    window_closed = pyqtSignal()   

    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.setWindowTitle("Alterar Usuário")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        self.widgets = {
                    "cmb_role":QComboBox(),
                    "inp_nome": QLineEdit(),
                    "inp_email":QLineEdit(),
                    "inp_senha":QLineEdit(),
                    "inp_endereco":QLineEdit(),
                    "btn_alterar":QPushButton("Alterar")   
                }
        
        usuarioRoles = UsuarioRoles.listar_usuarioRoles()
        for index,item in enumerate(usuarioRoles):
            self.widgets["cmb_role"].addItem(item[1], item[0])
            if self.usuario[4] == item[1]:
                self.widgets["cmb_role"].setCurrentIndex(index)
      
        self.widgets["inp_email"].setPlaceholderText("Email")
        self.widgets["inp_email"].setText(usuario[2])
        self.widgets["inp_senha"].setPlaceholderText("Digite a nova senha")
        self.widgets["inp_senha"].setEchoMode(QLineEdit.EchoMode.Password)
        self.widgets["inp_nome"].setPlaceholderText("Nome")
        self.widgets["inp_nome"].setText(usuario[1])
        self.widgets["inp_endereco"].setPlaceholderText("Endereço")
        self.widgets["inp_endereco"].setText(usuario[3]) 
        self.widgets["btn_alterar"].clicked.connect(self.btn_alterarClick)

        for w in self.widgets.values():
            self.layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)   


    def btn_alterarClick(self):
        cripto = Criptografia()
        if self.widgets["inp_senha"].text() == "":
            dadosCadastrais = {
                "role": self.widgets["cmb_role"].currentData(),
                "nome":  self.widgets["inp_nome"].text(),
                "email": self.widgets["inp_email"].text(),
                "endereco": self.widgets["inp_endereco"].text(),
                "usuarioID": self.usuario[0]
                }
            flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
            if flagPreenchido == False:
                    self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                    self.msg.show()
            else:
                Usuario.alterar_dados_usuario(dadosCadastrais["role"],dadosCadastrais["nome"],dadosCadastrais["email"], dadosCadastrais["endereco"],dadosCadastrais["usuarioID"])
                self.msg = MensagemWindow(False,"Dados cadastrados")
                self.msg.show()
                self.close()
        else:
            dadosCadastrais = {
                "role": self.widgets["cmb_role"].currentData(),
                "nome":  self.widgets["inp_nome"].text(),
                "email": self.widgets["inp_email"].text(),
                "senha": cripto.criptografar(self.widgets["inp_senha"].text()),
                "endereco": self.widgets["inp_endereco"].text(),
                "usuarioID": self.usuario[0]
                }   
            flagPreenchido = Utilities.verificarPreenchido(dadosCadastrais)
            if flagPreenchido == False:
                    self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
                    self.msg.show()
            else:
                Usuario.alterar_usuario(dadosCadastrais["role"],dadosCadastrais["nome"],dadosCadastrais["email"], dadosCadastrais["senha"],dadosCadastrais["endereco"],dadosCadastrais["usuarioID"])
                self.msg = MensagemWindow(False,"Dados cadastrados")
                self.msg.show()
                self.close()
            
    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)