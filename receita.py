from dbConnection import oracleConnection
from prettytable import PrettyTable

class receita:
    @staticmethod
    def cadastrar_receita():
        nome = str(input("Nome receita: ")).strip()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Receita(nome,valorVenda) values (:1, :2)', (nome, 0))
        OracleConnection.kill()

    @staticmethod
    def listar_receitas():
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT * FROM receita')
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista

    @staticmethod 
    def listar_receitas_pretty_table():
        table = PrettyTable()
        dados = receita.listar_receitas()
        table.field_names = ["ID", "Valor de venda", "Nome"]
        for row in dados:
            table.add_row(row)
        print(table)
        