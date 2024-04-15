from dbConnection import oracleConnection
from receita import receita
from datetime import date
from prettytable import PrettyTable

class lote:
    @staticmethod
    def cadastrar_lote():
        receita.listar_receitas_pretty_table()
        receitaID = int(input("ID Receita:"))
        quantidadeProduzida = int(input("Escolha a quantidade produzida: "))
        quantidadeRestante = quantidadeProduzida
        diaProducao = int(input("Dia da produção: "))
        mesProducao = int(input("Mes da produção:: "))
        anoProducao = int(input("Ano da produção: "))
        validadeDia = int(input("Dia vencimento validade: "))
        validadeMes = int(input("Mes vencimento validade: "))
        validadeAno = int(input("Ano vencimento validade: "))
        dataProducao = date(year = anoProducao, month= mesProducao, day= diaProducao)
        dataValidade = date(year= validadeAno, month= validadeMes, day= validadeDia)
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Insert into Lote(ReceitaID, DataProducao,DataValidade,QuantidadeProduzida,QuantidadeRestante)  values (:1, :2, :3, :4, :5)', (receitaID, dataProducao, dataValidade, quantidadeProduzida, quantidadeRestante))
        OracleConnection.kill()

    @staticmethod
    def listar_lote():
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('SELECT * FROM lote')
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_lote_pretty_table():
        table = PrettyTable()
        dados = lote.listar_lote()
        table.field_names = ["ID", "RECEITAID", "DATAPRODUCAO", "DATAVALIDADE", "VALORPRODUCAO", "CADASTROLOTEESTOQUECONCLUIDO", "QUANTIDADEPRODUZIDA", "QUANTIDADERESTANTE"]
        for row in dados:
            table.add_row(row)
        print(table)

