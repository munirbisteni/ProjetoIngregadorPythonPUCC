from dbConnection import OracleConnection
from ingrediente import Ingrediente
from receita import Receita
from prettytable import PrettyTable
from datetime import datetime

class ReceitaIngredientes:
    @staticmethod    
    def cadastrar_receitaIngredientes(receitaID, ingredienteID, quantidade):
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Insert into receitaIngredientes(receitaID, ingredienteID,quantidadeUsada) values (:1, :2, :3)', (receitaID,ingredienteID, quantidade))
        oracleConnection.connection.commit()
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
    def listar_receitaIngredientesByID(receitaID):
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""SELECT   
                                                ri.ReceitaIngredienteID, 
                                                i.nome, 
                                                ri.QuantidadeUsada,
                                                u.IDENTIFICADOR,
                                                i.alergenico
                                            FROM 
                                                receitaIngredientes ri
                                            INNER JOIN
                                                ingrediente i ON i.ingredienteID = ri.ingredienteID
                                            INNER JOIN
                                                unidade u ON u.unidadeID = i.unidadeID
                                            WHERE 
                                                (ri.Excluido = 0 or ri.Excluido IS NULL) AND  
                                                (ri.DATA_EXCLUSAO > :1 OR ri.DATA_EXCLUSAO IS NULL) AND
                                                ri.receitaID = :2
                                            """,(dataHoje, receitaID))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
            
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
      