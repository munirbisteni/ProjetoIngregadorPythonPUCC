import sys
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QMainWindow,
    QWidget,
)

from usuario import Usuario
from mensagemWindow import MensagemWindow
from .alterarUsuarioWindow import  AlterarUsuarioWindow


class ListarUsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listar Estoque")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.initUI()

    def initUI(self):
        self.populate_table()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    
    def populate_table(self):
        self.usuarios = Usuario.listar_usuarios()
        self.table_widget.setRowCount(len(self.usuarios))
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["Nome", "Email", "Endereço","Tipo" ,"Alterar", "Excluir"])

        for row, usuario in enumerate(self.usuarios):
            usuario_id_item = QTableWidgetItem(f"{usuario[1]}")
            self.table_widget.setItem(row, 0, usuario_id_item)

            nome_item = QTableWidgetItem(f"{usuario[2]}")
            self.table_widget.setItem(row, 1, nome_item)

            endereco_item = QTableWidgetItem(f"{usuario[3]}")
            self.table_widget.setItem(row, 2, endereco_item)

            role_item = QTableWidgetItem(f"{usuario[4]}")
            self.table_widget.setItem(row, 3, role_item)

            alterar_button = QPushButton("Alterar")
            alterar_button.clicked.connect(lambda _, e=usuario: self.alterar(e))
            self.table_widget.setCellWidget(row, 4, alterar_button)

            excluir_button = QPushButton("Excluir")
            excluir_button.clicked.connect(lambda _, e=usuario: self.excluir(e))
            self.table_widget.setCellWidget(row, 5, excluir_button)

    def alterar(self, usuario):
        self.selectedOption = AlterarUsuarioWindow(usuario)
        self.selectedOption.window_closed.connect(self.populate_table)
        self.selectedOption.show()
        print(f"Alterar Usuário: {usuario}")

    def excluir(self, usuario):
        Usuario.excluir_usuario(usuario[0])
        self.msg = MensagemWindow(False,f"usuario de id {usuario[0]} excluído com sucesso")
        self.msg.show()
        print(f"Excluir Usuário: {usuario}")
        self.populate_table()

