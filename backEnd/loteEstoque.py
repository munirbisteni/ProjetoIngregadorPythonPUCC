from dbConnection import OracleConnection
from estoque import Estoque
from prettytable import PrettyTable
from lote import Lote  
from datetime import datetime

class LoteEstoque:
    @staticmethod
    def cadastrar_loteEstoque(LoteID, EstoqueID):
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('INSERT INTO LoteEstoque(LoteID, EstoqueID) values (:1, :2)', (LoteID, EstoqueID))
            oracleConnection.kill()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def listar_loteEstoque():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT LoteEstoqueID, loteID, EstoqueID, QuantidadeUsada FROM loteEstoque WHERE (Excluido = 0 or Excluido IS NULL) and (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL)',(dataHoje,))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_loteEstoque_pretty_table():
        table = PrettyTable()
        dados = LoteEstoque.listar_loteEstoque()
        table.field_names = ["ID", "LOTEID", "ESTOQUEID", "QUANTIDADE USADA"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def excluir_loteEstoque():
        LoteEstoque.listar_loteEstoque_pretty_table()
        loteEstoqueID = int(input("ID do loteEstoque a ser excluído: "))
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update loteEstoque SET Excluido = :1, DATA_EXCLUSAO = :2  where loteEstoqueID = :3',(1, dataHoje, loteEstoqueID))
            oracleConnection.kill()
        except Exception as e:
            print("erro: Nâo foi possível excluir o loteEstoque")

