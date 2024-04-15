from dbConnection import oracleConnection
from ingrediente import ingrediente
from receita import receita
from prettytable import PrettyTable

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
                OracleConnection.cursor.execute('Insert into receitaIngredientes(receitaID,ingredienteID,quantidade) values (:1, :2)', (receitaID,ingredienteID, quantidade))
                OracleConnection.kill()
    
    @staticmethod
    def listar_receitaIngredientes():
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT * FROM receitaIngredientes')
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