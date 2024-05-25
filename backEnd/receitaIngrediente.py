from dbConnection import OracleConnection
from ingrediente import Ingrediente
from receita import Receita
from prettytable import PrettyTable
from datetime import datetime

class ReceitaIngredientes:
    @staticmethod    
    def cadastrar_receitaIngredientes():
        concluiuCadastroIngredientes = -1
        while concluiuCadastroIngredientes != 0:
            concluiuCadastroIngredientes = int(input("Cadastrar ingrediente(1), Cancelar cadastro de receita(2) Concluir cadastro de ingredientes (0)")) 
            if concluiuCadastroIngredientes == 2:
                return
            elif concluiuCadastroIngredientes != 0:
                Receita.listar_receitas_pretty_table()
                receitaID = int(input("Escolha o ID da receita que adicionará um item: "))
                Ingrediente.listar_ingredientes_pretty_table()
                ingredienteID = int(input("Escolha o ID do ingrediente que é usado na receita: "))
                quantidade = int(input("Escreva a quantidade que é usado do ingrediente na receita por unidade: "))
                oracleConnection = OracleConnection()
                oracleConnection.cursor.execute('Insert into receitaIngredientes(receitaID, ingredienteID,quantidadeUsada) values (:1, :2, :3)', (receitaID,ingredienteID, quantidade))
                oracleConnection.kill()
    
    @staticmethod
    def listar_receitaIngredientes():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT ReceitaIngredienteID, receitaID, IngredienteID, QuantidadeUsada FROM receitaIngredientes WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL)',(dataHoje,))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_receitaIngredientes_pretty_table():
        table = PrettyTable()
        dados = ReceitaIngredientes.listar_receitaIngredientes()
        table.field_names = ["ID", "RECEITAID", "INGREDIENTEID", "QUANTIDADE USADA"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def excluir_receitaIngrediente():
        ReceitaIngredientes.listar_receitaIngredientes_pretty_table()
        receitaIngredienteID = int(input("ID da receitaIngrediente a ser excluída: "))
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update receitaIngredientes SET Excluido = :1, DATA_EXCLUSAO = :2 where receitaIngredienteID = :3',(1, dataHoje, receitaIngredienteID))
            oracleConnection.kill()
        except Exception as e:
            print("erro: Nâo foi possível excluir a receitaIngrediente")
      