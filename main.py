from backEnd.estoque import Estoque
from backEnd.ingrediente import Ingrediente
from backEnd.lote import Lote
from backEnd.loteEstoque import LoteEstoque
from backEnd.receita import Receita
from backEnd.receitaIngrediente import ReceitaIngredientes
from backEnd.custosGerais import CustosGerais
def menu():
    print("1 - Receita:")
    print("2 - Ingrediente:")
    print("3 - receitaIngrediente:")
    print("4 - Lote:")
    print("5 - Estoque:")
    print("6 - LoteEstoque:")
    print("7 - CustosGerais:")
    print("0 - Sair")

def printOpcoes(nome):
    print(f"1 - Listar {nome}: ")
    print(f"2 - Cadastrar {nome}: ")
    print(f"3 - Excluir {nome}: ")
    print(f"0 - Voltar: ")
    return int(input("Sua escolha: "))

while True:
    menu()
    opcao = int(input("Digite sua escolha: "))
    if opcao == 0:
        break
    elif opcao == 1:
        innerOption = printOpcoes("receita")
        if innerOption == 1:
            if len(Receita.listar_receitas()) >= 1:
                Receita.listar_receitas_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos uma receita antes!")
                input("Enter para continuar")
        elif innerOption == 2:
            if len(Ingrediente.listar_ingredientes()) >= 1:
                Receita.cadastrar_receita()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
        elif innerOption == 3:
            if len(Ingrediente.listar_ingredientes()) >= 1:
                Receita.excluir_receita()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
    elif opcao == 2:
        innerOption = printOpcoes("ingrediente")
        if innerOption == 1:
            if len(Ingrediente.listar_ingredientes()) >= 1:
                Ingrediente.listar_ingredientes_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
        elif innerOption == 2:
            Ingrediente.cadastrar_ingrediente()
            input("Enter para continuar")
        elif innerOption == 3:
            if len(Ingrediente.listar_ingredientes()) >= 1:
                Receita.excluir_receita()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
    elif opcao == 3:
        innerOption = printOpcoes("receitaIngrediente")
        if innerOption == 1:
            if len(ReceitaIngredientes.listar_receitaIngredientes()) >= 1:
                ReceitaIngredientes.listar_receitaIngredientes_pretty_table()
            else:
                print("Cadastre ao menos uma receitaIngrediente antes!")
                input("Enter para continuar")
        elif innerOption == 2:
            if len(Receita.listar_receitas()) >= 1 and len(Ingrediente.listar_ingredientes()) >= 1:
                ReceitaIngredientes.cadastrar_receitaIngredientes()
            else:
                print("Cadastre ao menos uma receita e um ingrediente!")
                input("Enter para continuar")
        elif innerOption == 3:
            if len(ReceitaIngredientes.listar_receitaIngredientes() >= 1):
                ReceitaIngredientes.excluir_receitaIngrediente()
            else:
                print("Cadastre ao menos uma receitaIngrediente!")
                input("Enter para continuar")
    elif opcao == 4:
        innerOption = printOpcoes("lote")
        if innerOption == 1:
            if len(Lote.listar_lote()) >= 1:
                Lote.listar_lote_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um lote antes!")
                input("Enter para continuar")
        if innerOption == 2:
            if len(Receita.listar_receitas()) >=1:
                Lote.cadastrar_lote()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos uma receita antes!")
                input("Enter para continuar")
        if innerOption == 3:
            if len(Lote.listar_lote >= 1):
                Lote.excluir_lote()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um lote antes!")
                input("Enter para continuar")
    elif opcao == 5:
        innerOption = printOpcoes("estoque")
        if innerOption == 1:
            if len(Estoque.listar_estoque()) >= 1:
                Estoque.listar_estoque_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um estoque antes!")
        if innerOption == 2:
            if len(Ingrediente.listar_ingredientes()) >= 1:
                    Estoque.cadastrar_estoque()
                    input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
        if innerOption == 3:
            if len(Estoque.listar_estoque >= 1):
                Estoque.excluir_estoque()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um lote antes!")
                input("Enter para continuar")
    elif opcao == 6:
        innerOption = printOpcoes("loteEstoque")
        if innerOption == 1:
            if len(LoteEstoque.listar_loteEstoque()) >= 1:
                LoteEstoque.listar_loteEstoque_pretty_table()
            else:
                print("Cadastre ao menos um loteEstoque!")
                input("Enter para continuar")
        if innerOption == 2:
            if len(Lote.listar_lote()) >= 1 and len(Estoque.listar_estoque()) >= 1:
                LoteEstoque.cadastrar_loteEstoque()
            else:
                print("Cadastre ao menos um lote e um estoque!")
                input("Enter para continuar")
        if innerOption == 3:
            if len(LoteEstoque.listar_loteEstoque()) >= 1:
                LoteEstoque.excluir_loteEstoque()
            else:
                print("Cadastre ao menos um loteEstoque!")
    elif opcao == 7:
        print(f"1 - Alterar CustosGerais")
        print(f"2 - Listar CustosGerais")
        print(f"3 - Voltar ")
        innerOption = int(input("Sua escolha: "))
        if innerOption == 1:
            CustosGerais.alterarCustoGeral()
        elif innerOption == 2:
            CustosGerais.listar_custosGerais_pretty_table()