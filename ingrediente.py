from dbConnection import oracleConnection
from prettytable import PrettyTable
from unidade import unidade
class ingrediente:
    @staticmethod
    def cadastrar_ingrediente():
        nomeIngrediente = str(input("Nome do produto: ")).strip()
        alergenico = bool(input("É alergenico?(True/False)"))
        unidade.listar_unidade_pretty_table()
        unidadeID = int(input("Qual a unidade de medida desse ingrediente(id):"))
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Ingrediente(nome,alergenico,UnidadeID) values (:1, :2, :3)', (nomeIngrediente, alergenico, unidadeID))
        OracleConnection.kill()
    
    @staticmethod
    def listar_ingredientes():
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT * FROM ingrediente')
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_receitas_pretty_table():
        table = PrettyTable()
        dados = ingrediente.listar_ingredientes()
        table.field_names = ["ID", "NOME", "ALERGENICO", "UNIDADEID"]
        for row in dados:
            table.add_row(row)
        print(table)
    