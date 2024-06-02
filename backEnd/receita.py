from dbConnection import OracleConnection
from prettytable import PrettyTable
from datetime import datetime
from criptografia import Criptografia
import oracledb

class Receita:
    @staticmethod
    def cadastrar_receita(nome, descricao):
        oracleConnection = OracleConnection()

        try:
            receita_id = oracleConnection.cursor.var(oracledb.NUMBER)
            oracleConnection.cursor.execute('Insert into Receita(nome,valorVenda,descricao) values (:1, :2, :3) RETURNING receitaID INTO :4', (nome, 0,descricao, receita_id))
            oracleConnection.connection.commit()
            oracleConnection.kill()
            return receita_id.getvalue()[0]
        
        except Exception as e:
            print("Erro ao cadastrar receita:", e)
            return None


    @staticmethod
    def listar_receitas():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT ReceitaID, ValorVenda, Nome, Descricao FROM receita WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL )',(dataHoje,))
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()

        cripto = Criptografia()
        resultado = list(resultado)
        resultado = [list(row) for row in resultado]
        for index,item in enumerate(resultado):
            if resultado[index][3] is not None:
                resultado[index][3] = cripto.decriptografar(item[3])
            else:
                resultado[index][3] = "Não preenchido"
        return resultado

    @staticmethod 
    def listar_receitas_pretty_table():
        table = PrettyTable()
        dados = Receita.listar_receitas()
        table.field_names = ["ID", "Valor de venda", "Nome", "Descrição"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def excluir_receita(receitaID):
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update receita SET Excluido = :1, DATA_EXCLUSAO = :2 where receitaID = :3',(1, dataHoje, receitaID))
            oracleConnection.kill()
        except Exception as e:
            print("erro: Nâo foi possível excluir a receita")
      
    @staticmethod
    def alterar_receita(nome, descricao,valorVenda,receitaID):
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Update receita SET nome = :1, Descricao = :2, ValorVenda = :3 where receitaID = :4',(nome, descricao, valorVenda, receitaID))
        oracleConnection.connection.commit()
        oracleConnection.kill()