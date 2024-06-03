from dbConnection import OracleConnection
from criptografia import Criptografia
from datetime import datetime

class Usuario:
    @staticmethod
    def cadastrar_usuario_cliente(nome, email, senha, endereco, cidadeID):
        usuarioroleID = 3
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Insert into Usuario(nome,email,senha,cidadeID, endereco, usuarioroleID) values (:1, :2, :3, :4, :5, :6)', (nome,email, senha, cidadeID, endereco, usuarioroleID))
        oracleConnection.connection.commit()
        oracleConnection.kill()
            
    @staticmethod
    def cadastrar_usuario(role,nome, email, senha, endereco, cidadeID):
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Insert into Usuario(usuarioroleID, nome,email,senha,cidadeID, endereco) values (:1, :2, :3, :4, :5, :6)', (role,nome, email,senha, cidadeID, endereco))
        oracleConnection.connection.commit()
        oracleConnection.kill()
    
    @staticmethod
    def alterar_dados_usuario(role,nome, email, endereco, usuarioID):
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('UPDATE Usuario set nome = :1, email = :2, endereco = :4, usuarioRoleID = :5 where UsuarioID = :6 ', (nome, email, endereco, role, usuarioID))
        oracleConnection.connection.commit()
        oracleConnection.kill()

    @staticmethod
    def alterar_usuario(role,nome, email, senha, endereco, usuarioID):
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('UPDATE Usuario set nome = :1, email = :2, senha = :3, endereco = :4, usuarioRoleID = :5 where UsuarioID = :6 ', (nome, email,senha, endereco, role, usuarioID))
        oracleConnection.connection.commit()
        oracleConnection.kill()
        
    @staticmethod
    def listar_usuarios():
        dataHoje = datetime.now()
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Select u.usuarioID, u.Nome, u.email, u.endereco, r.Descricao, u.cidadeID from usuario u INNER JOIN UsuarioRoles r ON r.usuarioRoleID = u.UsuarioRoleID WHERE (u.Excluido = 0 or u.Excluido IS NULL) and  (u.DATA_EXCLUSAO > :1 OR u.DATA_EXCLUSAO IS NULL )', (dataHoje,))
        resultado = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return resultado

    def excluir_usuario(usuarioID):
        dataHoje = datetime.now()
        try:
            oracleConnection = OracleConnection()
            oracleConnection.cursor.execute('Update usuario SET Excluido = :1, DATA_EXCLUSAO = :2  where loteID = :3',(1, dataHoje, usuarioID))
            oracleConnection.kill()    
        except Exception as e:
            print("erro: Nâo foi possível excluir o ususário")

    @staticmethod
    def validar_login(login, senha):
        cripto = Criptografia()
        senhaCriptografada = cripto.criptografar(senha)
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Select ur.Identificador, u.usuarioID from Usuario u INNER JOIN UsuarioRoles ur ON ur.UsuarioRoleID = u.usuarioRoleID where u.email = :1 and u.senha = :2 order by u.nome FETCH FIRST 1 ROW ONLY',(login,senhaCriptografada))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        if len(lista) > 0:
            return lista[0]
        return False
            
    


