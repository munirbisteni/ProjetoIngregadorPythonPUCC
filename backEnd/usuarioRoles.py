from dbConnection import OracleConnection
from datetime import datetime

class UsuarioRoles:
    @staticmethod
    def listar_usuarioRoles():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Select usuarioRoleID, descricao from UsuarioRoles WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL )', (dataHoje,))
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return resultado        