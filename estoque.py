from dbConnection import oracleConnection
from ingrediente import ingrediente
from datetime import date
from datetime import datetime
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
                ingrediente.listar_ingredientes_pretty_table()
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
        dataHoje = datetime.now()
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT EstoqueID, IngredienteID, QuantidadeComprada, QuantidadeRestante,DataValidade, ValorCompra FROM Estoque WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL)',(dataHoje,))
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

    @staticmethod
    def excluir_estoque():
        estoque.listar_estoque_pretty_table()
        estoqueID = int(input("ID do estoque a ser excluído: "))
        dataHoje = datetime.now()
        try:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('Update estoque SET Excluido = :1, DATA_EXCLUSAO = :2  where estoqueID = :3',(1, dataHoje, estoqueID))
            OracleConnection.kill()
        except Exception as e:
            print("erro: Nâo foi possível excluir o estoque")
