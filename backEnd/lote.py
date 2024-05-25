from dbConnection import oracleConnection
from receita import Receita
from datetime import date
from prettytable import PrettyTable
from datetime import datetime
class Lote:
    @staticmethod
    def cadastrar_lote():
        Receita.listar_receitas_pretty_table()
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
        dataHoje = datetime.now()
        OracleConnection.cursor.execute('SELECT loteID,ReceitaID, DataProducao, DataValidade, ValorProducao, CadastroLoteEstoqueConcluido, QUantidadeProduzida, QuantidadeRestante FROM lote WHERE (Excluido = 0 or Excluido IS NULL) and  (DATA_EXCLUSAO > :1 OR DATA_EXCLUSAO IS NULL)',(dataHoje,))
        lista = OracleConnection.cursor.fetchall()
        OracleConnection.kill()
        return lista
    
    @staticmethod
    def listar_lote_pretty_table():
        table = PrettyTable()
        dados = Lote.listar_lote()
        table.field_names = ["ID", "RECEITAID", "DATAPRODUCAO", "DATAVALIDADE", "VALORPRODUCAO", "CADASTROLOTEESTOQUECONCLUIDO", "QUANTIDADEPRODUZIDA", "QUANTIDADERESTANTE"]
        for row in dados:
            table.add_row(row)
        print(table)

    @staticmethod
    def excluir_lote():
        Lote.listar_lote_pretty_table()
        loteID = int(input("ID do lote a ser excluído: "))
        dataHoje = datetime.now()
        try:
            OracleConnection = oracleConnection()
            OracleConnection.cursor.execute('Update lote SET Excluido = :1, DATA_EXCLUSAO = :2  where loteID = :3',(1, dataHoje, loteID))
            OracleConnection.kill()    
        except Exception as e:
            print("erro: Nâo foi possível excluir o lote")

    @staticmethod
    def alterar_ValorProducao():
        Lote.listar_lote_pretty_table()
        loteID = int(input("ID do lote a ser excluída: "))
        novoValor = float(input("Novo valor de produção do lote: "))
        OracleConnection = oracleConnection()
        OracleConnection.cursor.execute('Update lote SET ValorProducao = :1 where loteID = :2'(novoValor, loteID))
        OracleConnection.kill()