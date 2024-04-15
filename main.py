from estoque import estoque
from ingrediente import ingrediente
from lote import lote
from loteEstoque import loteEstoque
from receita import receita
from receitaIngrediente import receitaIngredientes
from custosGerais import custosGerais
def exibir_menu():
    print("1 - Cadastrar Receita")
    print("2 - Listar Receitas")
    print("3 - Cadastrar Lote")
    print("4 - Listar Lote")
    print("5 - Cadastrar Ingrediente")
    print("6 - Listar ingredientes")
    print("7 - Cadastrar Estoque")
    print("8 - Listar Estoque")
    print("9 - Cadastrar LoteEstoque") 
    print("10 - Listar LoteEstoque")
    print("11 - alterar Custos Gerais")
    print("12 - listar custos gerais")
    print("13 - Cadastar receitaIngredientes")
    print("14 - Listar ReceitaIngredientes")
    print("0 - Sair")

while True:
    exibir_menu()
    opcao = int(input("Digite sua escolha: "))
    if opcao == 0:
        break
    elif opcao == 1:
        if len(ingrediente.listar_ingredientes()) >= 1:
            receita.cadastrar_receita()
            input("Enter para continuar")
        else:
            print("Cadastre ao menos um ingrediente antes!")
            input("Enter para continuar")
    elif opcao == 2:
        if len(receita.listar_receitas()) >= 1:
            receita.listar_receitas_pretty_table()
            input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 3:
        if len(receita.listar_receitas()) >= 1 and len(receitaIngredientes.listar_receitaIngredientes()) >= 1:
            lote.cadastrar_lote()
            input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes e um estoque antes!")
            input("Enter para continuar")
    elif opcao == 4:
        if len(lote.listar_lote()) >= 1:
                lote.listar_lote_pretty_table()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 5:
        ingrediente.cadastrar_ingrediente()
        input("Enter para continuar")
    elif opcao == 6:
        if len(ingrediente.listar_ingredientes) >= 1:
                ingrediente.listar_receitas_pretty_table()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos um ingrediente antes!")
            input("Enter para continuar")
    elif opcao == 7:
        if len(ingrediente.listar_ingredientes()) >= 1:
                estoque.cadastrar_estoque()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 8:
        if len(estoque.listar_estoque()) >= 1:
                estoque.listar_estoque_pretty_table()
                input("Enter para continuar")
    elif opcao == 9:
        if len(lote.listar_lote()) >= 1 and len(estoque.listar_estoque()) >= 1:
             loteEstoque.cadastrar_loteEstoque()
        else:
            print("Cadastre ao menos um lote e um estoque!")
            input("Enter para continuar")
    elif opcao == 10:
        if len(loteEstoque.listar_loteEstoque()) >= 1:
             loteEstoque.listar_loteEstoque_pretty_table()
        else:
            print("Cadastre ao menos um loteEstoque!")
            input("Enter para continuar")
    elif opcao == 11:
        custosGerais.alterarCustoGeral()
        input("Enter para continuar")
    elif opcao == 12:
        custosGerais.listar_custosGerais_pretty_table()
        input("Enter para continuar")
    elif opcao == 13:
        if len(receita.listar_receitas()) >= 1 and len(ingrediente.listar_ingredientes()) >= 1:
             receitaIngredientes.cadastrar_receitaIngredientes()
        else:
            print("Cadastre ao menos um lote e um estoque!")
            input("Enter para continuar")
    elif opcao == 14:
        if len(receitaIngredientes.listar_receitaIngredientes()) >= 1:
             receitaIngredientes.listar_receitaIngredientes_pretty_table()
        else:
            print("Cadastre ao menos um loteEstoque!")
            input("Enter para continuar")
    else:
        print("Cadastre ao menos uma receita antes!")
        input("Enter para continuar")
    