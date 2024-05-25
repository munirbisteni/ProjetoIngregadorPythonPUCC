from dbConnection import OracleConnection
from criptografia import Criptografia
class Usuario:
    @staticmethod
    def cadastrar_usuario_cliente(nome, email, senha, endereco, cidadeID):
        usuarioroleID = 3
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Insert into Usuario(nome,email,senha,cidadeID, endereco, usuarioroleID) values (:1, :2, :3, :4, :5, :6)', (nome,email, senha, cidadeID, endereco, usuarioroleID))
        oracleConnection.kill()
    
    @staticmethod
    def cadastrar_usuario_funcionario():
        nome = input("Escreva o seu nome:")
        senha = input("Escreva a sua senha:")
        cripto = Criptografia()
        senha = cripto.criptografar_dado(senha)
        #cidade.listar_cidade_pretty_table()
        cidadeID = input("escreva o número da sua cidade:")
        endereco = input("escreva o seu endereço")
        usuarioroleID = 2
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Insert into Usuario(nome,senha,cidadeID, endereco, usuarioroleID) values (:1, :2, :3, :4, :5)', (nome, senha, cidadeID, endereco, usuarioroleID))
        oracleConnection.kill()
    
    @staticmethod
    def cadastrar_usuario_administrador():
        nome = input("Escreva o seu nome:")
        senha = input("Escreva a sua senha:")
        cripto = Criptografia()
        senha = cripto.criptografar_dado(senha)
        #cidade.listar_cidade_pretty_table()
        cidadeID = input("escreva o número da sua cidade:")
        endereco = input("escreva o seu endereço")
        usuarioroleID = 1
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Insert into Usuario(nome,senha,cidadeID, endereco, usuarioroleID) values (:1, :2, :3, :4, :5)', (nome, senha, cidadeID, endereco, usuarioroleID))
        oracleConnection.kill()

    @staticmethod
    def validar_login(login, senha):
        cripto = Criptografia()
        senhaCriptografada = cripto.criptografar(senha)
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('Select ur.Identificador from Usuario u INNER JOIN UsuarioRoles ur ON ur.UsuarioRoleID = u.usuarioRoleID where u.email = :1 and u.senha = :2 order by u.nome FETCH FIRST 1 ROW ONLY',(login,senhaCriptografada))
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        if len(lista) > 0:
            return lista[0][0]
        return False
            
    


