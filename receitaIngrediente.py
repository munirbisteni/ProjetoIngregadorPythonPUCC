from dbConnection import oracleConnection
from ingrediente import ingrediente
from receita import receita
from prettytable import PrettyTable
from datetime import datetime

class receitaIngredientes:
    @staticmethod    
    def cadastrar_receitaIngredientes():
        concluiuCadastroIngredientes = -1
        while concluiuCadastroIngredientes != 0:
            concluiuCadastroIngredientes = int(input("Cadastrar ingrediente(1), Cancelar cadastro de receita(2) Concluir cadastro de ingredientes (0)")) 
            if concluiuCadastroIngredientes == 2:
                return
            elif concluiuCadastroIngredientes != 0:
                receita.listar_receitas_pretty_table()
                receitaID = int(input("Escolha o ID da receita que adicionará um item: "))
                ingrediente.listar_receitas_pretty_table()
                ingredienteID = int(input("Escolha o ID do ingrediente que é usado na receita: "))
                quantidade = int(input("Escreva a quantidade que é usado do ingrediente na receita por unidade: "))
                OracleConnection = oracleConnection()
                OracleConnection.cursor.execute('Insert into receitaIngredientes(receitaID, ingredienteID,quantidadeUsada) values (:1, :2, :3)', (receitaID,ingredienteID, quantidade))
                OracleConnection.kill()
    
    @staticmethod
    def listar_receitaIngredientes():
        dataHoje = datetime.now()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT ReceitaIngredienteID, receitaID, IngredienteID, QuantidadeUsada FROM receitaIngredientes WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL)',(dataHoje,))
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_receitaIngredientes_pretty_table():
        table = PrettyTable()
        dados = receitaIngredientes.listar_receitaIngredientes()
        table.field_names = ["ID", "RECEITAID", "INGREDIENTEID", "QUANTIDADE USADA"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def excluir_receitaIngrediente():
        receitaIngredientes.listar_receitaIngredientes_pretty_table()
        receitaIngredienteID = int(input("ID da receitaIngrediente a ser excluída: "))
        dataHoje = datetime.now()
        try:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('Update receitaIngredientes SET Excluido = :1, DATA_EXCLUSAO = :2 where receitaIngredienteID = :3',(1, dataHoje, receitaIngredienteID))
            OracleConnection.kill()
        except Exception as e:
            print("erro: Nâo foi possível excluir a receitaIngrediente")
      