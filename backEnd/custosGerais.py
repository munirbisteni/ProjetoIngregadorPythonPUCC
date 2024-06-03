from dbConnection import OracleConnection
from prettytable import PrettyTable

class CustosGerais:
    @staticmethod
    def alterar_custos_gerais(ML,CF, IMP):
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute("""UPDATE custosGerais set VALORPORCENTAGEM = :1 where IDENTIFICADOR = 'ML'""", (ML, ))
        oracleConnection.connection.commit()
        oracleConnection.cursor.execute("""UPDATE custosGerais set VALORPORCENTAGEM = :1 where IDENTIFICADOR = 'CF'""", (CF, ))
        oracleConnection.connection.commit()
        oracleConnection.cursor.execute("""UPDATE custosGerais set VALORPORCENTAGEM = :1 where IDENTIFICADOR = 'IMPOSTO'""", (IMP, ))
        oracleConnection.connection.commit()
        oracleConnection.kill()

    @staticmethod
    def listar_custosGerais():
        oracleConnection = OracleConnection()
        oracleConnection.cursor.execute('SELECT CustoGeralID, Descricao, ValorPorcentagem, Identificador FROM CustosGerais')
        lista = oracleConnection.cursor.fetchall()
        oracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_custosGerais_pretty_table():
        table = PrettyTable()
        dados = CustosGerais.listar_custosGerais()
        table.field_names = ["ID", "DESCRICAO", "PROCENTAGEM %", "IDENTIFICADOR"]
        for row in dados:
            table.add_row(row)
        print(table)