from dbConnection import oracleConnection
from prettytable import PrettyTable

class unidade:
    @staticmethod
    def listar_unidade():
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT * FROM unidade')
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_unidade_pretty_table():
        table = PrettyTable()
        dados = unidade.listar_unidade()
        table.field_names = ["ID", "DESCRICAO", "IDENTIFICADOR"]
        for row in dados:
            table.add_row(row)
        print(table)
    