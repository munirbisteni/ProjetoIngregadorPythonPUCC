from dbConnection import oracleConnection
from estoque import estoque
from prettytable import PrettyTable
from lote import lote  
from datetime import datetime

class loteEstoque:
    @staticmethod
    def cadastrar_loteEstoque():
        LoteID = -1
        concluiuCadastroIngredientes = 1
        while concluiuCadastroIngredientes != 0:
            concluiuCadastroIngredientes = int(input("Cadastrar ingrediente do estoque(1), Cancelar cadastro de lote(2) Concluir cadastro de ingredientes do estoque(0): ")) 
            if concluiuCadastroIngredientes == 2:
                return
            if concluiuCadastroIngredientes != 0:
                lote.listar_lote_pretty_table()
                LoteID = int(input("Escolha o ID lote que deseja cadastrar: "))
                estoque.listar_estoque_pretty_table()
                EstoqueID = int(input("Escolha o Estoque usado: "))
                try:
                    OracleConnection = oracleConnection()
                    OracleConnection.cursor.execute('INSERT INTO LoteEstoque(LoteID, EstoqueID) values (:1, :2)', (LoteID, EstoqueID))
                    OracleConnection.kill()
                except Exception as e:
                    print("occoreu um erro ao cadastrar este loteEstoque, verifique a validade dos dados!")
                    print("Verifique se o ingrediente é usado na receita referente ao lote!")
                    print("Verifique também se o estoque contém quantidade suficiente para a produção desse lote!")

        if LoteID != -1:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('UPDATE Lote set CADASTROLOTEESTOQUECONCLUIDO = :1 WHERE LOTEID = :2', (1, LoteID))
            OracleConnection.kill()
    
    @staticmethod
    def listar_loteEstoque():
        dataHoje = datetime.now()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT LoteEstoqueID, loteID, EstoqueID, QuantidadeUsada FROM loteEstoque WHERE (Excluido = 0 or Excluido = NULL) and dataExclusao > :1'(dataHoje))
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_loteEstoque_pretty_table():
        table = PrettyTable()
        dados = loteEstoque.listar_loteEstoque()
        table.field_names = ["ID", "LOTEID", "ESTOQUEID", "QUANTIDADE USADA"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def excluir_loteEstoque():
        loteEstoque.listar_loteEstoque_pretty_table()
        loteEstoqueID = int(input("ID do loteEstoque a ser excluído: "))
        dataHoje = datetime.now()
        try:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('Update loteEstoque SET Excluido = :1, dataExclusao = :2  where loteEstoqueID = :3'(1, dataHoje, loteEstoqueID))
        except Exception as e:
            print("erro: Nâo foi possível excluir o ingrediente")

