from dbConnection import oracleConnection
from prettytable import PrettyTable

class custosGerais:
    @staticmethod
    def alterarCustoGeral():
        custosGerais.listar_custosGerais_pretty_table()
        custoID = int(input("Qual o custo geral que você deseja alterar(id):"))
        porcentagem = float(input("Qual a nova porcentagem que ira substituir o valor atual(use '.' como separador, ex: 75.00):"))
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('UPDATE custosGerais set VALORPORCENTAGEM = :1 where CUSTOGERALID = :2', (porcentagem, custoID))
        OracleConnection.kill()

    @staticmethod
    def listar_custosGerais():
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT CustoGeralID, Descricao, ValorPorcentagem, Identificador FROM CustosGerais')
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_custosGerais_pretty_table():
        table = PrettyTable()
        dados = custosGerais.listar_custosGerais()
        table.field_names = ["ID", "DESCRICAO", "PROCENTAGEM %", "IDENTIFICADOR"]
        for row in dados:
            table.add_row(row)
        print(table)
        # if print(dados[0][2]) < 100:
        #     print(f"Lucro: {dados[0][2]} Lucro muito alto!")