import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QMainWindow
from PyQt6 import QtCore

class MensagemWindow(QMainWindow):
    def __init__(self, erro:bool, mensagem:str):
        super().__init__()

        self.setWindowTitle("Mensagem")
        self.setGeometry(100, 100, 300, 150)


        layout = QVBoxLayout()
        self.widgets = {
            "lbl_mensagem": QLabel(mensagem),
            "btn_fechar":QPushButton("Fechar")
        }
        self.widgets["lbl_mensagem"].setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        if erro == False:
            self.widgets["lbl_mensagem"].setStyleSheet("color: green")  # Define o estilo para sucesso
        elif erro == True:
            self.widgets["lbl_mensagem"].setStyleSheet("color: red")  # Define o estilo para sucesso
        
        self.widgets["btn_fechar"].clicked.connect(self.fecharJanela)

        for w in self.widgets.values():
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def fecharJanela(self): 
        self.close()

