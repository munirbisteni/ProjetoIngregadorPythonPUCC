from dbConnection import OracleConnection
from prettytable import PrettyTable
from unidade import Unidade
from datetime import datetime
class Ingrediente:
    @staticmethod
    def cadastrar_ingrediente():
        nomeIngrediente = str(input("Nome do ingrediente: ")).strip()
        lista = Ingrediente.listar_ingredientes()
        for item in lista:
            if item[1] == nomeIngrediente:
                print("Ingrediente já cadastrado!")
                return

        alergenico = bool(input("É alergenico?(True/False)"))
        Unidade.listar_unidade_pretty_table()
        unidadeID = int(input("Qual a unidade de medida desse ingrediente(id):"))
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Insert into Ingrediente(nome,alergenico,UnidadeID) values (:1, :2, :3)', (nomeIngrediente, alergenico, unidadeID))
        oracleConnection.kill()
    
    @staticmethod
    def listar_ingredientes():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT i.IngredienteID, i.Nome, i.Alergenico, u.IDENTIFICADOR FROM ingrediente i INNER JOIN Unidade u ON u.unidadeID = i.unidadeID WHERE (i.Excluido = 0 or i.Excluido IS NULL) and (i.DATA_EXCLUSAO > :1 OR i.DATA_EXCLUSAO IS NULL)',(dataHoje,))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_ingredientes_pretty_table():
        table = PrettyTable()
        dados = Ingrediente.listar_ingredientes()
        table.field_names = ["ID", "NOME", "ALERGENICO", "UNIDADEID"]
        for row in dados:
            table.add_row(row)
        print(table)
    
    @staticmethod
    def excluir_ingrediente():
        Ingrediente.listar_receitas_pretty_table()
        ingredienteID = int(input("ID do ingrediente a ser excluído: "))
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update ingrediente SET Excluido = :1, DATA_EXCLUSAO = :2  where ingredienteID = :3',(1, dataHoje, ingredienteID))
            oracleConnection.kill()
        except Exception as e:
            print("erro: Nâo foi possível excluir o ingrediente")
