from estoque import estoque
from ingrediente import ingrediente
from lote import lote
from loteEstoque import loteEstoque
from receita import receita
from receitaIngrediente import receitaIngredientes
def exibir_menu():
    print("1 - Cadastrar Receita")
    print("2 - Listar Receitas")
    print("3 - Cadastrar Lote")
    print("4 - Listar Lote")
    print("5 - Cadastrar Ingrediente")
    print("6 - Listar ingredientes")
    print("7 - Cadastrar Estoque")
    print("8 - Listar Estoque")
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
            receita.listar_receitas()
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
                lote.listar_lote()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 5:
        ingrediente.cadastrar_ingrediente()
        input("Enter para continuar")
    elif opcao == 6:
        if len(ingrediente.listar_ingredientes) >= 1:
                ingrediente.listar_ingredientes()
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
                estoque.listar_estoque()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
