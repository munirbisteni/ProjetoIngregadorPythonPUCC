def cadastro_produto(p):
    produtoid = int(input("ID produto: "))
    nomeproduto = str(input("Nome produto: ")).strip()
    valorprod = float(input("Valor de Venda: R$"))
    p.append((produtoid, nomeproduto, valorprod))
    print("Cadastro realizado com sucesso!!\n\n")


def exibir_menu():
    print("1-Cadastrar produto\n2-Cadastrar item\n3-Excluir produto\n4-Editar estoque\n6-Conta\n5-Sair\n\n")


def cadastro_item(i, p):
    itemid = int(input("ID item: "))
    for produto in p:
        produtoid, nomeproduto, valorprod = produto
        if produtoid == itemid:
            valoritem = float(input("Valor de producao item: "))
            dataprod = float(input("Data de producao item: "))
            qtdestoque = int(input("Quantidade em estoque: "))
            i.append((itemid, valoritem, dataprod, qtdestoque))


def exc_produto(p):
    for produto in p:
        print(produto)
        produtoid, nomeproduto, valorprod = produto
        proddel = int(input("Digite o id do produto ou 0 para o proximo: "))
        if produtoid == proddel:
            p.remove(produto)
            print("Produto excluido com sucesso!!\n\n")


def estoque(ing):
    parar = 1
    while parar != 0:
        parar = int(input("Cadastrar novo ingrediente (1), atualizar estoque (2) ou sair(0)"))
        if parar == 0:
            break
        elif parar == 1:
            id_ingrediente = int(input("Id do ingrediente: "))
            nome_ing = str(input("Nome do produto: ")).strip()
            preco_ing = float(input("Preco total pago: R$"))
            qtd_ing = float(input("Quantidade em Kg ou L comprado: "))
            dia_valid_ing = int(input("Dia vencimento validade: "))
            mes_valid_ing = int(input("Mes vencimento validade: "))
            ano_valid_ing = int(input("Ano vencimento validade: "))
            ing.append((id_ingrediente, nome_ing, preco_ing, qtd_ing, dia_valid_ing, mes_valid_ing, ano_valid_ing))
        elif parar == 2:
            for ingredientes in ing:
                id_ingrediente, nome_ing, preco_ing, qtd_ing, dia_valid_ing, mes_valid_ing, ano_valid_ing = ingredientes
                id_procura = int(input("Id do produto desejado: "))
                if id_procura == id_ingrediente:
                    remover = int(input("Quantidade de produtos que deseja remover: "))
                    qtd_ing = qtd_ing - remover
                    adicionar = int(input("Quantidade de produtos que deseja adicionar: "))
                    qtd_ing = qtd_ing + adicionar
                    dia_valid_ing = int(input("Dia vencimento validade: "))
                    mes_valid_ing = int(input("Mes vencimento validade: "))
                    ano_valid_ing = int(input("Ano vencimento validade: "))


def contas(p):
    for produtos in p:
        produtoid, nomeproduto, valorprod = produtos
        busca_id = int(input("Id do produto desejado: "))
        qtd_item = int(input("Quantidade de itens feitos por receita: "))
        if busca_id == produtoid:
            ML = float(input("Margem de lucro liquida: "))
            ML = valorprod * ML/100
            CF = ML*0.15
            IMP = ML*0.12
            PV = (ML + CF + IMP + valorprod)/qtd_item


produtos = []
item = []
ingredientes = []
while True:
    exibir_menu()
    opcao = int(input("Digite sua escolha: "))
    if opcao == 5:
        break
    elif opcao == 1:
        cadastro_produto(produtos)
    elif opcao == 2:
        cadastro_item(item, produtos)
    elif opcao == 3:
        exc_produto(produtos)
    elif opcao == 4:
        estoque(ingredientes)
    elif opcao == 6:
        contas(produtos)
