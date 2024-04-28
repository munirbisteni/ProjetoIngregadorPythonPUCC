from dbConnection import oracleConnection
from prettytable import PrettyTable
from datetime import datetime
from criptografia import Criptografia
class receita:
    @staticmethod
    def cadastrar_receita():
        nome = str(input("Nome receita: ")).strip()
        descricao = str(input("De uma descição breve da receita (max 50 caractéres):")).strip()
        cripto = Criptografia()
        descricao = cripto.criptografar(descricao)
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Receita(nome,valorVenda,descricao) values (:1, :2, :3)', (nome, 0,descricao))
        OracleConnection.kill()

    @staticmethod
    def listar_receitas():
        dataHoje = datetime.now()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT ReceitaID, ValorVenda, Nome, Descricao FROM receita WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL )',(dataHoje,))
        resultado = OracleConnection.cursor.fetchall()
        OracleConnection.kill()

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
        dados = receita.listar_receitas()
        table.field_names = ["ID", "Valor de venda", "Nome", "Descrição"]
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
            OracleConnection.cursor.execute('Update receita SET Excluido = :1, DATA_EXCLUSAO = :2 where receitaID = :3',(1, dataHoje, receitaID))
            OracleConnection.kill()
        except Exception as e:
            print("erro: Nâo foi possível excluir a receita")
      
    @staticmethod
    def alterar_ValorVenda():
        receita.listar_receitas_pretty_table()
        receitaID = int(input("ID da receita a ser excluída: "))
        novoValor = float(input("Novo valor de venda da receita: "))
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Update receita SET ValorVenda = :1 where receitaID = :2',(novoValor, receitaID))
  