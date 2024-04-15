from dbConnection import oracleConnection
from prettytable import PrettyTable
from datetime import datetime

class receita:
    @staticmethod
    def cadastrar_receita():
        nome = str(input("Nome receita: ")).strip()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Receita(nome,valorVenda) values (:1, :2)', (nome, 0))
        OracleConnection.kill()

    @staticmethod
    def listar_receitas():
        dataHoje = datetime.now()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT ReceitaID, ValorVenda, Nome FROM receita WHERE (Excluido = 0 or Excluido = NULL) and dataExclusao > :1'(dataHoje))
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

    @staticmethod
    def excluir_receita():
        receita.listar_receitas_pretty_table()
        receitaID = int(input("ID da receita a ser excluída: "))
        dataHoje = datetime.now()
        try:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('Update receita SET Excluido = :1, dataExclusao = :2 where receitaID = :3'(1, dataHoje, receitaID))
        except Exception as e:
            print("erro: Nâo foi possível excluir o ingrediente")
      