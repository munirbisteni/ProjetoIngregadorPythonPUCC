from dbConnection import OracleConnection
from receita import Receita
from datetime import date
from prettytable import PrettyTable
from datetime import datetime
import oracledb
class Lote:
    @staticmethod
    def cadastrar_lote(receitaID, dtProducao, dtVencimento, qtdProduzida):
        Receita.listar_receitas_pretty_table()
        dataProducao = dtProducao.toPyDate()
        dataValidade = dtVencimento.toPyDate()
        qtdRestante = qtdProduzida
        oracleConnection = OracleConnection()
        
        try:            
            lote_id = oracleConnection.cursor.var(oracledb.NUMBER)
            oracleConnection.cursor.execute("INSERT INTO Lote(ReceitaID, DataProducao, DataValidade, QuantidadeProduzida, QuantidadeRestante)VALUES (:1, :2, :3, :4, :5)RETURNING LoteID INTO :6", (receitaID, dataProducao, dataValidade, qtdProduzida, qtdRestante, lote_id))
            oracleConnection.connection.commit()
            oracleConnection.kill()
            
            return lote_id.getvalue()[0]
        
        except Exception as e:
            print("Erro ao cadastrar lote:", e)
            return None
        
    @staticmethod
    def listar_lote():
        oracleConnection = OracleConnection()
        dataHoje = datetime.now()
        oracleConnection.cursor.execute("""SELECT 
                                            l.loteID,
                                            l.ReceitaID,
                                            r.nome, 
                                            l.DataProducao, 
                                            l.DataValidade, 
                                            l.ValorProducao, 
                                            l.QUantidadeProduzida, 
                                            l.QuantidadeRestante 
                                        FROM 
                                            lote l
                                        INNER JOIN
                                            receita r on r.receitaID = l.receitaID
                                        WHERE 
                                            (l.Excluido = 0 or l.Excluido IS NULL) and  
                                            (l.DATA_EXCLUSAO > :1 OR l.DATA_EXCLUSAO IS NULL) and
                                            (l.CadastroLoteEstoqueConcluido = 1) ORDER BY l.LOTEID
                                        """,(dataHoje,))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_lote_pretty_table():
        table = PrettyTable()
        dados = Lote.listar_lote()
        table.field_names = ["ID", "RECEITAID", "DATAPRODUCAO", "DATAVALIDADE", "VALORPRODUCAO", "CADASTROLOTEESTOQUECONCLUIDO", "QUANTIDADEPRODUZIDA", "QUANTIDADERESTANTE"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def excluir_lote(loteID):
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update lote SET Excluido = :1, DATA_EXCLUSAO = :2  where loteID = :3',(1, dataHoje, loteID))
            oracleConnection.kill()    
        except Exception as e:
            print("erro: Nâo foi possível excluir o lote")

    @staticmethod
    def alterar_ValorProducao():
        Lote.listar_lote_pretty_table()
        loteID = int(input("ID do lote a ser excluída: "))
        novoValor = float(input("Novo valor de produção do lote: "))
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Update lote SET ValorProducao = :1 where loteID = :2',(novoValor, loteID))
        oracleConnection.connection.commit()
        oracleConnection.kill()

    @staticmethod
    def atualizar_lote(loteID, receitaID, dtProducao, dtVencimento, qtdProduzida):
        Receita.listar_receitas_pretty_table()
        dataProducao = dtProducao.toPyDate()
        dataValidade = dtVencimento.toPyDate()
        qtdRestante = qtdProduzida
        oracleConnection = OracleConnection()
        
        try:            
            oracleConnection.cursor.execute("""UPDATE Lote
                                                SET receitaID = :1,
                                                    dataProducao = :2,
                                                    dataValidade = :3,
                                                    QuantidadeRestante = :4
                                                WHERE
                                                    loteID = :5""", (receitaID, dataProducao, dataValidade, qtdRestante, loteID))
            oracleConnection.connection.commit()
            oracleConnection.kill()
            return True
        
        except Exception as e:
            print("Erro ao alterar lote:", e)
            return False
        


    @staticmethod
    def definir_CadastroConcluidoLote(LoteID):
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Update lote SET CADASTROLOTEESTOQUECONCLUIDO = 1 where loteID = :1', (LoteID,))
        oracleConnection.connection.commit()
        oracleConnection.kill()