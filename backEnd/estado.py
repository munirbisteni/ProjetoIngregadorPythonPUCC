from dbConnection import OracleConnection
from datetime import date
from datetime import datetime

class Estado:
    @staticmethod
    def cadastrar_estado():
        pass

    @staticmethod
    def listar_estados():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT EstadoID, UF, nome FROM Estado WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL)',(dataHoje,))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    
    @staticmethod
    def excluir_estado():
        pass

    @staticmethod
    def alterar_estado():
        pass