from dbConnection import OracleConnection
from estoque import Estoque
from prettytable import PrettyTable
from lote import Lote  
from datetime import datetime

class LoteEstoque:
    @staticmethod
    def cadastrar_loteEstoque():
        LoteID = -1
        concluiuCadastroIngredientes = 1
        while concluiuCadastroIngredientes != 0:
            concluiuCadastroIngredientes = int(input("Cadastrar ingrediente do estoque(1), Cancelar cadastro de lote(2) Concluir cadastro de ingredientes do estoque(0): ")) 
            if concluiuCadastroIngredientes == 2:
                return
            if concluiuCadastroIngredientes != 0:
                Lote.listar_lote_pretty_table()
                LoteID = int(input("Escolha o ID lote que deseja cadastrar: "))
                Estoque.listar_estoque_pretty_table()
                EstoqueID = int(input("Escolha o Estoque usado: "))
                try:
                    oracleConnection = OracleConnection()
                    oracleConnection.cursor.execute('INSERT INTO LoteEstoque(LoteID, EstoqueID) values (:1, :2)', (LoteID, EstoqueID))
                    oracleConnection.kill()
                except Exception as e:
                    print("occoreu um erro ao cadastrar este loteEstoque, verifique a validade dos dados!")
                    print("Verifique se o ingrediente é usado na receita referente ao lote!")
                    print("Verifique também se o estoque contém quantidade suficiente para a produção desse lote!")

        if LoteID != -1:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('UPDATE Lote set CADASTROLOTEESTOQUECONCLUIDO = :1 WHERE LOTEID = :2', (1, LoteID))
            oracleConnection.kill()
    
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

