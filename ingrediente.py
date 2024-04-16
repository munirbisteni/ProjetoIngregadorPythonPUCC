from dbConnection import oracleConnection
from prettytable import PrettyTable
from unidade import unidade
from datetime import datetime
class ingrediente:
    @staticmethod
    def cadastrar_ingrediente():
        nomeIngrediente = str(input("Nome do ingrediente: ")).strip()
        lista = ingrediente.listar_ingredientes()
        for item in lista:
            if item[1] == nomeIngrediente:
                print("Ingrediente já cadastrado!")
                return

        alergenico = bool(input("É alergenico?(True/False)"))
        unidade.listar_unidade_pretty_table()
        unidadeID = int(input("Qual a unidade de medida desse ingrediente(id):"))
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Ingrediente(nome,alergenico,UnidadeID) values (:1, :2, :3)', (nomeIngrediente, alergenico, unidadeID))
        OracleConnection.kill()
    
    @staticmethod
    def listar_ingredientes():
        dataHoje = datetime.now()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT IngredienteID, Nome, Alergenico, UnidadeID FROM ingrediente WHERE (Excluido = 0 or Excluido IS NULL) and (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL)',(dataHoje,))
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_ingredientes_pretty_table():
        table = PrettyTable()
        dados = ingrediente.listar_ingredientes()
        table.field_names = ["ID", "NOME", "ALERGENICO", "UNIDADEID"]
        for row in dados:
            table.add_row(row)
        print(table)
    
    @staticmethod
    def excluir_ingrediente():
        ingrediente.listar_receitas_pretty_table()
        ingredienteID = int(input("ID do ingrediente a ser excluído: "))
        dataHoje = datetime.now()
        try:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('Update ingrediente SET Excluido = :1, DATA_EXCLUSAO = :2  where ingredienteID = :3',(1, dataHoje, ingredienteID))
        except Exception as e:
            print("erro: Nâo foi possível excluir o ingrediente")
