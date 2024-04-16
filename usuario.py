from dbConnection import oracleConnection
from criptografia import criptografia
class usuario:
    @staticmethod
    def cadastrar_usuario_cliente():
        nome = input("Escreva o seu nome:")
        senha = input("Escreva a sua senha:")
        senha = criptografia.criptografar_dado(senha)
        #cidade.listar_cidade_pretty_table()
        cidadeID = input("escreva o número da sua cidade:")
        endereco = input("escreva o seu endereço")
        usuarioroleID = 3
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Usuario(nome,senha,cidadeID, endereco, usuarioroleID) values (:1, :2, :3, :4, :5)', (nome, senha, cidadeID, endereco, usuarioroleID))
        OracleConnection.kill()
    
    @staticmethod
    def cadastrar_usuario_funcionario():
        nome = input("Escreva o seu nome:")
        senha = input("Escreva a sua senha:")
        senha = criptografia.criptografar_dado(senha)
        #cidade.listar_cidade_pretty_table()
        cidadeID = input("escreva o número da sua cidade:")
        endereco = input("escreva o seu endereço")
        usuarioroleID = 2
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Usuario(nome,senha,cidadeID, endereco, usuarioroleID) values (:1, :2, :3, :4, :5)', (nome, senha, cidadeID, endereco, usuarioroleID))
        OracleConnection.kill()
    
    @staticmethod
    def cadastrar_usuario_administrador():
        nome = input("Escreva o seu nome:")
        senha = input("Escreva a sua senha:")
        senha = criptografia.criptografar_dado(senha)
        #cidade.listar_cidade_pretty_table()
        cidadeID = input("escreva o número da sua cidade:")
        endereco = input("escreva o seu endereço")
        usuarioroleID = 1
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Usuario(nome,senha,cidadeID, endereco, usuarioroleID) values (:1, :2, :3, :4, :5)', (nome, senha, cidadeID, endereco, usuarioroleID))
        OracleConnection.kill()
    


