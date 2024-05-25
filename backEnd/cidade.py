from dbConnection import OracleConnection
from datetime import datetime

class Cidade:
    @staticmethod
    def cadastrar_cidade():
        pass

    @staticmethod
    def get_cidade_by_EstadoID(estadoID):
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT CidadeID, nome FROM cidade WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL) and (estadoID = :2)',(dataHoje, estadoID))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    

    @staticmethod
    def excluir_cidade():
        pass

    @staticmethod
    def alterar_cidade():
        pass