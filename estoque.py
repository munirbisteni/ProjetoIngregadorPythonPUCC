from dbConnection import oracleConnection
from ingrediente import ingrediente
from datetime import date
from prettytable import PrettyTable

class estoque:
    @staticmethod
    def cadastrar_estoque():
        parar = 1
        while parar != 0:
            parar = int(input("Listar ingredientes(1),Cadastrar novo ingrediEnteEstoque (2) ou sair(3): "))
            if parar == 3:
                break
            elif parar == 1:
                ingrediente.listar_receitas_pretty_table()
            elif parar == 2:
                ingredienteID = int(input("Id do ingrediente: "))
                valorDeCompra = float(input("Preco total pago: R$"))
                quantidadeComprada = float(input("Quantidade comprada: "))
                validadeDia = int(input("Dia vencimento validade: "))
                validadeMes = int(input("Mes vencimento validade: "))
                validadeAno = int(input("Ano vencimento validade: "))
                validade = date(year=validadeAno, month=validadeMes, day=validadeDia)
                quantidadeRestante = quantidadeComprada
                OracleConnection = oracleConnection()
                OracleConnection.cursor.execute('Insert into Estoque(IngredienteID, QuantidadeComprada, QuantidadeRestante, DataValidade, ValorCompra) values (:1, :2, :3, :4, :5)', (ingredienteID, quantidadeComprada, quantidadeRestante, validade, valorDeCompra))
                OracleConnection.kill()

    @staticmethod
    def listar_estoque():
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT * FROM Estoque')
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_estoque_pretty_table():
        table = PrettyTable()
        dados = estoque.listar_estoque()
        table.field_names = ["ID", "INGREDIENTE ID", "QUANTIDADE COMPRADA", "QUANTIDADE RESTANTE", "DATA VALIDADE", "VALOR DA COMPRA"]
        for row in dados:
            table.add_row(row)
        print(table)
