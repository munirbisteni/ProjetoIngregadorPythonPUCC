from dbConnection import OracleConnection
from datetime import datetime
import oracledb

class Pedido:
    @staticmethod
    def listar_pedidosVenda(vendaID):
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""SELECT 
                                                p.pedidoID, 
                                                p.ValorVenda, 
                                                p.QUANTIDADE,
                                                r.Nome
                                            FROM 
                                                Pedido p 
                                            INNER JOIN
                                                receita r ON r.receitaID = p.receitaID
                                            WHERE 
                                                (p.Excluido = 0 OR p.Excluido IS NULL) AND 
                                                (p.DATA_EXCLUSAO > :1 OR p.DATA_EXCLUSAO IS NULL) AND
                                                p.vendaID = :2 
                                            ORDER BY 
                                                p.pedidoID""",
                                        (dataHoje, vendaID))
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return resultado
    @staticmethod
    def listar_vendas():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""SELECT 
                                                v.vendaID, 
                                                v.VALORTOTALVENDA,
                                                st.descricao,
                                                v.STATUSVENDAID
                                            FROM 
                                                venda v 
                                            INNER JOIN
                                                STATUSVENDA st ON st.STATUSVENDAID = v.STATUSVENDAID
                                            WHERE 
                                                (v.Excluido = 0 OR v.Excluido IS NULL) AND 
                                                (v.DATA_EXCLUSAO > :1 OR v.DATA_EXCLUSAO IS NULL) """,(dataHoje, ))
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return resultado     
    @staticmethod
    def listar_vendasByUserID(clienteID):
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""SELECT 
                                                v.vendaID, 
                                                v.VALORTOTALVENDA,
                                                st.descricao,
                                                v.STATUSVENDAID
                                            FROM 
                                                venda v 
                                            INNER JOIN
                                                STATUSVENDA st ON st.STATUSVENDAID = v.STATUSVENDAID
                                            WHERE 
                                                (v.Excluido = 0 OR v.Excluido IS NULL) AND 
                                                (v.DATA_EXCLUSAO > :1 OR v.DATA_EXCLUSAO IS NULL) AND
                                                v.usuarioID = :2 """,(dataHoje, clienteID))
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return resultado     
    @staticmethod
    def listar_vendaByID(vendaID):
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""SELECT 
                                                v.vendaID, 
                                                v.VALORTOTALVENDA,
                                                st.descricao,
                                                v.STATUSVENDAID
                                            FROM 
                                                venda v 
                                            INNER JOIN
                                                STATUSVENDA st ON st.STATUSVENDAID = v.STATUSVENDAID
                                            WHERE 
                                                (v.Excluido = 0 OR v.Excluido IS NULL) AND 
                                                (v.DATA_EXCLUSAO > :1 OR v.DATA_EXCLUSAO IS NULL) AND
                                                v.vendaID = :2 """,(dataHoje, vendaID))
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return resultado     
    @staticmethod
    def excluir_itemPedido(pedidoID):
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update pedido SET Excluido = :1, DATA_EXCLUSAO = :2  where pedidoID = :3',(1, dataHoje, pedidoID))
            oracleConnection.kill()    
        except Exception as e:
            print("erro: Nâo foi possível excluir o pedido")

    @staticmethod
    def cadastrar_venda(clienteID):
        oracleConnection = OracleConnection()
        try:            
            vendaID = oracleConnection.cursor.var(oracledb.NUMBER)
            oracleConnection.cursor.execute("INSERT INTO Venda(VALORTOTALVENDA, USUARIOID, STATUSVENDAID)VALUES (:1, :2, :3)RETURNING vendaID INTO :4", (0, clienteID,8,vendaID))
            oracleConnection.connection.commit()
            oracleConnection.kill()
            
            return vendaID.getvalue()[0]
        
        except Exception as e:
            print("Erro ao cadastrar lote:", e)
            return None
    
    @staticmethod
    def cadastrar_pedidoItem(vendaID, receitaID, quantidade):
        oracleConnection = OracleConnection()
        try:            
            oracleConnection.cursor.execute("INSERT INTO pedido(VENDAID, VALORVENDA, RECEITAID, QUANTIDADE)VALUES (:1, :2, :3, :4)", (vendaID, 0,receitaID,quantidade))
            oracleConnection.connection.commit()
            oracleConnection.kill()
            return None
        except Exception as e:
            error, = e.args
            oracleConnection.kill()
            if error.code == 20001:
                return "Erro ao cadastrar pedido: Não há estoque suficiente."
            else:
                return f"Erro ao cadastrar pedido: {error.message}, contate nosso suporte"
            
    @staticmethod
    def cancelar_venda(vendaID):
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update venda SET STATUSVENDAID = :1  where vendaID = :3',(5 ,vendaID))
            oracleConnection.connection.commit()
            oracleConnection.kill()    
        except Exception as e:
            print("erro: Nâo foi possível excluir o pedido")
    
    @staticmethod
    def listar_statusVenda():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""SELECT 
                                                statusVendaID, 
                                                identificador                
                                            FROM 
                                                statusVenda """)
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return resultado            
    
    @staticmethod
    def alterar_status(vendaID, statusID):
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update venda SET STATUSVENDAID = :1  where vendaID = :3',(statusID ,vendaID))
            oracleConnection.connection.commit()
            oracleConnection.kill()    
        except Exception as e:
            print("erro: Nâo foi possível excluir o pedido")