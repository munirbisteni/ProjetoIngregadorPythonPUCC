receitas = []
lote = []
ingredientes = []
ingredientesEstoque = []

#def cadastrar_receita:
def cadastrar_receita():
    receitaID = int(input("ID receita: "))
    nome = str(input("Nome receita: ")).strip()
    valorVenda = -1
    concluiuCadastroIngredientes = -1
    receitaIngredientes = []
    quantidadeIngredientes = []
    while concluiuCadastroIngredientes != 0:
        concluiuCadastroIngredientes = int(input("Cadastrar ingrediente(1), Cancelar cadastro de receita(2) Concluir cadastro de ingredientes (0)")) 
        if concluiuCadastroIngredientes == 2:
            return
        elif concluiuCadastroIngredientes != 0:
            listar_ingredientes()
            receitaIngredientes.append(int(input("Escolha o ID do ingrediente que é usado na receita: ")))
            quantidadeIngredientes.append(int(input("Escreva a quantidade que é usado do ingrediente na receita por unidade: ")))
    receitas.append([receitaID, nome, valorVenda, receitaIngredientes, quantidadeIngredientes])
    print("Cadastro realizado com sucesso!!\n\n")


def listar_receitas():
    for r in receitas:
        print("ID: " + str(r[0]) + "; Nome:" + str(r[1]))
        if r[2] == -1:
            print("nenhum lote cadastrado para poder definir o valor!")
        else:
            print("Valor de venda:" + str(r[2]))
        print("lista de ingredientes: ")
        for i in range(len(r[3])):
            nomeIngrediente = ""
            for ingrediente in ingredientes:
                if ingrediente[0] == r[3][i]:
                    nomeIngrediente = ingrediente[1]
            if nomeIngrediente != "":
                print(("Ingrediente: " + nomeIngrediente + "; Quantidade: "+ str(r[4][i])))
            else:
                print("Ingrediente: " + str(r[3][i]) + "; Quantidade: "+ str(r[4][i])+ "-> ATENÇÃO ITEM COM ID INCORRETAMENTE CADASTRADO")
            

def cadastrar_lote():
    print("Listagem das receitas: ")
    listar_receitas()

    loteID = int(input("ID lote: "))
    receitaID = int(input("ID Receita:"))
    receitaPosicao = 0
    validado = False
    
    for i in range(len(receitas)):
        if receitas[i][0] == receitaID:
            validado = True
            receitaPosicao = i
    if validado == False:
        print("Voce escolheu um ID inválido de receita!")
        return

    quantidadeProduzida = int(input("Escolha a quantidade produzida: "))

    loteIngredienteIDs = []
    concluiuCadastroIngredientes = 1
    while concluiuCadastroIngredientes != 0:
        concluiuCadastroIngredientes = int(input("Cadastrar ingrediente do estoque(1), Cancelar cadastro de lote(2) Concluir cadastro de ingredientes do estoque(0): ")) 
        if concluiuCadastroIngredientes == 2:
            return
        if concluiuCadastroIngredientes != 0:
            listar_estoque()
            loteIngredienteID = int(input("Escolha o ID do estoque ingrediente que é usado na receita: "))
            
            validado = False
            for ingredienteEs in ingredientesEstoque:
                if ingredienteEs[0] == loteIngredienteID:
                    for i in range(len(receitas[receitaPosicao][3])):
                            if receitas[receitaPosicao][3][i] == ingredienteEs[1]:
                                somatoriaRestante = ingredienteEs[7] - (receitas[receitaPosicao][4][i] * quantidadeProduzida)
                                if somatoriaRestante < 0:
                                    validado = False
                                else:
                                    ingredienteEs[7] = somatoriaRestante
                                    validado = True
            if validado == False:
                print("Voce escolheu um ID inválido de o estoque, ou o item não está na receita ou a quantidade em estoque é menor do que a dita usada!")
                return
            loteIngredienteIDs.append(loteIngredienteID)

    valorProducao = 0
    for l in loteIngredienteIDs:
        for i in ingredientesEstoque:
            if i[0] == l:
                precoUnitario = i[2]
                for r in receitas:
                    if r[0] == receitaID:
                        for y in range(len(r[3])):
                            if r[3][y] == i[0]:
                                valorProducao += r[4][y] * precoUnitario * quantidadeProduzida
    
    quantidadeRestante = quantidadeProduzida
    diaProducao = int(input("Dia da produção: "))
    mesProducao = int(input("Mes da produção:: "))
    anoProducao = int(input("Ano da produção: "))
    validadeDia = int(input("Dia vencimento validade: "))
    validadeMes = int(input("Mes vencimento validade: "))
    validadeAno = int(input("Ano vencimento validade: "))
    dataProducao = str(str(diaProducao) + "/"+ str(mesProducao) + "/" + str(anoProducao))
    dataValidade = str(str(validadeDia) + "/"+ str(validadeMes) + "/" + str(validadeAno))

    valorVendaUn = gerarValorVenda(valorProducao, quantidadeProduzida)
    for r in receitas:
        if r[0] == receitaID:
            if r[2] < valorVendaUn:
                r[2] = valorVendaUn

    lote.append((loteID, receitaID, loteIngredienteIDs, quantidadeProduzida, valorProducao, quantidadeRestante,dataProducao, dataValidade))

def listar_lote():
    for l in lote:
        print("ID:" + str(l[0]) + " ; ID da receita:" + str(l[1]) + " ; LoteIngrediente IDs: " + str(l[2]) + " ;Quantidade Produzida: " + str(l[3]) + "; Valor Producao: " + str(l[4]) + "; Quantidade Restante:" + str(l[5]) + "; Data de producao:" + str(l[6]) + "; Data de validade:" + str(l[7]))
def exc_receita():
    while True:
        listar_receitas()
        prodDel = int(input("Digite o ID da receita ou -1 para sair: "))
        if prodDel == -1:
            return
        for r in receitas:
            if r[0] == prodDel:
                receitas.remove(r)
                print("Produto excluido com sucesso!!\n\n")

def cadastrar_ingrediente():
    idIngrediente = int(input("Id do ingrediente: "))
    nomeIngrediente = str(input("Nome do produto: ")).strip()
    alergenico = bool(input("É alergenico?(True/False)"))
    ingredientes.append((idIngrediente, nomeIngrediente, alergenico))

def listar_ingredientes():
    for i in ingredientes:
        print("ID: " + str(i[0]) + "; nome: " + str(i[1]) + "; alergênico: " + str(i[2]))

def listar_estoque():
    nomeIngrediente = ""
    for i in ingredientesEstoque:
        for ingrediente in ingredientes:
                    if ingrediente[0] == i[1]:
                        nomeIngrediente = ingrediente[1]
        if nomeIngrediente != "":
            print("ID: " + str(i[0]) + "; ingrediente: " + nomeIngrediente + "; precoUnitario: " + str(i[2]) + "; Quantidade comprada: " + str(i[3]) + "; Data de validade: " + str(i[4]) + "/" + str(i[5]) + "/" + str(i[6]))
        else:
            print("ID: " + str(i[0]) + "; ingrediente: " + str(i[1]) + "; precoUnitario: " + str(i[2]) + "; Quantidade comprada: " + str(i[3]) + "; Data de validade: " + str(i[4]) + "/" + str(i[5]) + "/" + str(i[6]) + "-> ATENCAO ID DO INGREDIENTE INEXISTENTE")

def cadastrar_estoque():
    parar = 1
    while parar != 0:
        parar = int(input("Listar ingredientes(1),Cadastrar novo ingrediEnteEstoque (2) ou sair(3): "))
        if parar == 3:
            break
        elif parar == 1:
            listar_ingredientes()
        elif parar == 2:
            ingredienteEstoqueID = int(input("Id do ingredienteEstoque: "))
            ingredienteID = int(input("Id do ingrediente: "))
            precoUnitario = float(input("Preco total pago: R$"))
            quantidade = float(input("Quantidade em Kg ou L comprado: "))
            precoUnitario = precoUnitario/quantidade
            validadeDia = int(input("Dia vencimento validade: "))
            validadeMes = int(input("Mes vencimento validade: "))
            validadeAno = int(input("Ano vencimento validade: "))
            quantidadeRestante = quantidade
            ingredientesEstoque.append([ingredienteEstoqueID, ingredienteID, precoUnitario, quantidade, validadeDia, validadeMes, validadeAno, quantidadeRestante])
        # elif parar == 2:
        #     for ingredientes in ing:
        #         id_ingrediente, nome_ing, preco_ing, qtd_ing, dia_valid_ing, mes_valid_ing, ano_valid_ing = ingredientes
        #         id_procura = int(input("Id do produto desejado: "))
        #         if id_procura == id_ingrediente:
        #             remover = int(input("Quantidade de produtos que deseja remover: "))
        #             qtd_ing = qtd_ing - remover
        #             adicionar = int(input("Quantidade de produtos que deseja adicionar: "))
        #             qtd_ing = qtd_ing + adicionar
        #             dia_valid_ing = int(input("Dia vencimento validade: "))
        #             mes_valid_ing = int(input("Mes vencimento validade: "))
        #             ano_valid_ing = int(input("Ano vencimento validade: "))


def gerarValorVenda(valorProducao, qtdProduzida):
    ML = 150
    ML = valorProducao * ML/100
    CF = ML*0.15
    IMP = ML*0.12
    return (ML + CF + IMP + valorProducao)/qtdProduzida

def exibir_menu():
    print("1 - Cadastrar Receita")
    print("2 - Listar Receitas")
    print("3 - Cadastrar Lote")
    print("4 - Listar Lote")
    print("5 - Cadastrar Ingrediente")
    print("6 - Listar ingredientes")
    print("7 - Cadastrar Estoque")
    print("8 - Listar Estoque")
    print("9 - Excluir Receita")
    print("0 - Sair")

while True:
    exibir_menu()
    opcao = int(input("Digite sua escolha: "))
    if opcao == 0:
        break
    elif opcao == 1:
        if len(ingredientes) >= 1:
            cadastrar_receita()
            input("Enter para continuar")
        else:
            print("Cadastre ao menos um ingrediente antes!")
            input("Enter para continuar")
    elif opcao == 2:
        if len(receitas) >= 1:
            listar_receitas()
            input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 3:
        if len(receitas) >= 1 and len(ingredientesEstoque) >= 1:
            cadastrar_lote()
            input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes e um estoque antes!")
            input("Enter para continuar")
    elif opcao == 4:
        if len(receitas) >= 1:
                listar_lote()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 5:
        cadastrar_ingrediente()
        input("Enter para continuar")
    elif opcao == 6:
        if len(ingredientes) >= 1:
                listar_ingredientes()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos um ingrediente antes!")
            input("Enter para continuar")
    elif opcao == 7:
        if len(ingredientes) >= 1:
                cadastrar_estoque()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 8:
        if len(ingredientesEstoque) >= 1:
                listar_estoque()
                input("Enter para continuar")
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")
    elif opcao == 9:
        if len(receitas) >= 1:
                exc_receita()
        else:
            print("Cadastre ao menos uma receita antes!")
            input("Enter para continuar")