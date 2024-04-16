from estoque import estoque
from ingrediente import ingrediente
from lote import lote
from loteEstoque import loteEstoque
from receita import receita
from receitaIngrediente import receitaIngredientes
from custosGerais import custosGerais
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
            if len(receita.listar_receitas()) >= 1:
                receita.listar_receitas_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos uma receita antes!")
                input("Enter para continuar")
        elif innerOption == 2:
            if len(ingrediente.listar_ingredientes()) >= 1:
                receita.cadastrar_receita()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
        elif innerOption == 3:
            if len(ingrediente.listar_ingredientes()) >= 1:
                receita.excluir_receita()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
    elif opcao == 2:
        innerOption = printOpcoes("ingrediente")
        if innerOption == 1:
            if len(ingrediente.listar_ingredientes()) >= 1:
                ingrediente.listar_ingredientes_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
        elif innerOption == 2:
            ingrediente.cadastrar_ingrediente()
            input("Enter para continuar")
        elif innerOption == 3:
            if len(ingrediente.listar_ingredientes()) >= 1:
                receita.excluir_receita()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
    elif opcao == 3:
        innerOption = printOpcoes("receitaIngrediente")
        if innerOption == 1:
            if len(receitaIngredientes.listar_receitaIngredientes()) >= 1:
                receitaIngredientes.listar_receitaIngredientes_pretty_table()
            else:
                print("Cadastre ao menos uma receitaIngrediente antes!")
                input("Enter para continuar")
        elif innerOption == 2:
            if len(receita.listar_receitas()) >= 1 and len(ingrediente.listar_ingredientes()) >= 1:
                receitaIngredientes.cadastrar_receitaIngredientes()
            else:
                print("Cadastre ao menos uma receita e um ingrediente!")
                input("Enter para continuar")
        elif innerOption == 3:
            if len(receitaIngredientes.listar_receitaIngredientes() >= 1):
                receitaIngredientes.excluir_receitaIngrediente()
            else:
                print("Cadastre ao menos uma receitaIngrediente!")
                input("Enter para continuar")
    elif opcao == 4:
        innerOption = printOpcoes("lote")
        if innerOption == 1:
            if len(lote.listar_lote()) >= 1:
                lote.listar_lote_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um lote antes!")
                input("Enter para continuar")
        if innerOption == 2:
            if len(receita.listar_receitas()) >=1:
                lote.cadastrar_lote()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos uma receita antes!")
                input("Enter para continuar")
        if innerOption == 3:
            if len(lote.listar_lote >= 1):
                lote.excluir_lote()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um lote antes!")
                input("Enter para continuar")
    elif opcao == 5:
        innerOption = printOpcoes("estoque")
        if innerOption == 1:
            if len(estoque.listar_estoque()) >= 1:
                estoque.listar_estoque_pretty_table()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um estoque antes!")
        if innerOption == 2:
            if len(ingrediente.listar_ingredientes()) >= 1:
                    estoque.cadastrar_estoque()
                    input("Enter para continuar")
            else:
                print("Cadastre ao menos um ingrediente antes!")
                input("Enter para continuar")
        if innerOption == 3:
            if len(estoque.listar_estoque >= 1):
                estoque.excluir_estoque()
                input("Enter para continuar")
            else:
                print("Cadastre ao menos um lote antes!")
                input("Enter para continuar")
    elif opcao == 6:
        innerOption = printOpcoes("loteEstoque")
        if innerOption == 1:
            if len(loteEstoque.listar_loteEstoque()) >= 1:
                loteEstoque.listar_loteEstoque_pretty_table()
            else:
                print("Cadastre ao menos um loteEstoque!")
                input("Enter para continuar")
        if innerOption == 2:
            if len(lote.listar_lote()) >= 1 and len(estoque.listar_estoque()) >= 1:
                loteEstoque.cadastrar_loteEstoque()
            else:
                print("Cadastre ao menos um lote e um estoque!")
                input("Enter para continuar")
        if innerOption == 3:
            if len(loteEstoque.listar_loteEstoque()) >= 1:
                loteEstoque.excluir_loteEstoque()
            else:
                print("Cadastre ao menos um loteEstoque!")
    elif opcao == 7:
        print(f"1 - Alterar CustosGerais")
        print(f"2 - Listar CustosGerais")
        print(f"3 - Voltar ")
        innerOption = int(input("Sua escolha: "))
        if innerOption == 1:
            custosGerais.alterarCustoGeral()
        elif innerOption == 2:
            custosGerais.listar_custosGerais_pretty_table()