from dbConnection import oracleConnection
from prettytable import PrettyTable
from datetime import datetime

class unidade:
    @staticmethod
    def listar_unidade():
        dataHoje = datetime.now()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT UnidadeID, Descricao, Identificador FROM unidade WHERE (Excluido = 0 or Excluido = NULL) and dataExclusao > :1'(dataHoje))
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
    
    @staticmethod
    def excluir_unidade():
        unidade.listar_unidade_pretty_table()
        unidadeID = int(input("ID da Unidade a ser excluída: "))
        dataHoje = datetime.now()
        try:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('Update unidade SET Excluido = :1, dataExclusao = :2 where unidadeID = :3'(1, dataHoje, unidadeID))
        except Exception as e:
            print("erro: Nâo foi possível excluir o ingrediente")
      