from dbConnection import OracleConnection
from ingrediente import Ingrediente
from datetime import date
from datetime import datetime
from prettytable import PrettyTable

class Estoque:
    @staticmethod
    def cadastrar_estoque(ingredienteID,validade,quantidadeComprada,valorCompra):
            try:
                validade = validade.toPyDate()
                quantidadeRestante = quantidadeComprada
                oracleConnection = OracleConnection()
                oracleConnection.cursor.execute('Insert into Estoque(IngredienteID, QuantidadeComprada, QuantidadeRestante, DataValidade, ValorCompra) values (:1, :2, :3, :4, :5)', (ingredienteID, quantidadeComprada, quantidadeRestante, validade, valorCompra))
                oracleConnection.kill()
                return True
            except Exception as e:
                print(e)
                return False
    @staticmethod
    def listar_estoque():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""SELECT 
                                            e.EstoqueID, 
                                            i.nome, 
                                            e.QuantidadeComprada, 
                                            e.QuantidadeRestante,
                                            e.DataValidade, 
                                            e.ValorCompra,
                                            u.IDENTIFICADOR
                                        FROM 
                                            Estoque e
                                        INNER JOIN 
                                            Ingrediente i ON i.ingredienteID = e.ingredienteID 
                                        INNER JOIN
                                            unidade u ON u.unidadeID = i.unidadeID
                                        WHERE 
                                            (e.Excluido = 0 or e.Excluido IS NULL) and  
                                            (e.DATA_EXCLUSAO > :1 OR e.DATA_EXCLUSAO IS NULL) ORDER BY e.estoqueID DESC""",(dataHoje,))
        
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    
    @staticmethod
    def excluir_estoque(EstoqueID):
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update Estoque SET Excluido = :1, DATA_EXCLUSAO = :2  where EstoqueID = :3',(1, dataHoje, EstoqueID))
            oracleConnection.kill()    
        except Exception as e:
            print("erro: Nâo foi possível excluir o Estoque")
    
    @staticmethod
    def listar_estoque_pretty_table():
        table = PrettyTable()
        dados = Estoque.listar_estoque()
        table.field_names = ["ID", "INGREDIENTE ID", "QUANTIDADE COMPRADA", "QUANTIDADE RESTANTE", "DATA VALIDADE", "VALOR DA COMPRA"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def alterar_estoque(estoqueID, dtValidade,QuantidadeRestante):
        dtValidade = dtValidade.toPyDate()
        oracleConnection = OracleConnection()
        try:            
            oracleConnection.cursor.execute("""UPDATE Estoque
                                                SET DATAVALIDADE = :1,
                                                    QUANTIDADERESTANTE = :2
                                                WHERE
                                                    ESTOQUEID = :3""", (dtValidade, QuantidadeRestante, estoqueID,))
            oracleConnection.connection.commit()
            oracleConnection.kill()
            return True
        except Exception as e:
            print("Erro ao alterar estoque:", e)
            return False
                
    @staticmethod
    def listar_estoque_by_receita(receitaID):
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT i.nome, e.EstoqueID, e.IngredienteID, e.QuantidadeComprada, e.QuantidadeRestante, e.DataValidade, e.ValorCompra FROM Estoque e INNER JOIN receitaIngredientes ri ON ri.ingredienteID = e.ingredienteID INNER JOIN ingrediente i ON i.ingredienteID = ri.ingredienteID  WHERE (e.Excluido = 0 or e.Excluido IS NULL) and  (e.DATA_EXCLUSAO > :1 OR e.DATA_EXCLUSAO IS NULL) and (ri.Excluido = 0 or ri.Excluido IS NULL) AND (ri.DATA_EXCLUSAO > :2 OR ri.DATA_EXCLUSAO IS NULL) and ri.receitaID = :3 AND e.quantidadeRestante > 0',(dataHoje,dataHoje,receitaID))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
