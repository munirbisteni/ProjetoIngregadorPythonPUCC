import sys

sys.path.append('./backEnd')
from usuario import Usuario

from PyQt6.QtCore import Qt
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

from funcionario.mainFuncionarioWindow import MainFuncionarioWindow
from cliente.mainClienteWindow import ClienteWindow
from admin.mainAdminWindow import MainAdminWindow
from registrarClienteWindow import MainRegistrarCliente
from mensagemWindow import MensagemWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login - Esfirras do Munir")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.widgets = {
            "inp_email":QLineEdit(),
            "inp_senha":QLineEdit(),
            "btn_login":QPushButton("Entrar"),
            "btn_registrar":QPushButton("Ainda não tenho conta")
        }
        self.widgets["inp_email"].setPlaceholderText("Email")

        self.widgets["inp_senha"].setPlaceholderText("Senha")
        self.widgets["inp_senha"].setEchoMode(QLineEdit.EchoMode.Password)
    
        self.widgets["btn_login"].clicked.connect(self.btn_entrarClick)
        self.widgets["btn_registrar"].clicked.connect(self.btn_registrarClick)

        for w in self.widgets.values():
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)   

    def btn_entrarClick(self):
        email = self.widgets["inp_email"].text()
        senha = self.widgets["inp_senha"].text()

        if email.strip() == "" or senha.strip() == "":
            self.msg = MensagemWindow(True,"Preencha todos os campos primeiramente")
            self.msg.show()
        else:
            self.validarLogin(email,senha)

    def validarLogin(self,email,senha):
        response = Usuario.validar_login(email,senha)
        if response != False:
            self.close()
            if response[0] == "CLIENTE":
                self.loginSucces = ClienteWindow(response[1])
                self.loginSucces  .show()
            elif response[0] == "FUNCIONARIO":
                self.loginSucces = MainFuncionarioWindow()
                self.loginSucces.show()
            elif response[0] == "ADMIN":
                self.loginSucces = MainAdminWindow()
                self.loginSucces.show()
            else:
                self.msg = MensagemWindow(True,"Ocorreu um erro interno, contate nosso suporte técnico")
                self.msg.show()                
        else:
            self.msg = MensagemWindow(True,"Usuário ou senha incorretos")
            self.msg.show()
            
    def btn_registrarClick(self):
        self.secondWindow = MainRegistrarCliente()
        self.secondWindow.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
