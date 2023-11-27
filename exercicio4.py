def cadastrar_produto(lista):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    
    produto = {"Nome": nome, "Preço": preco, "Quantidade": quantidade}
    lista.append(produto)
    print(f"\nProduto {nome} cadastrado com sucesso!\n")


def listar_produtos(lista):
    if not lista:
        print("\nLista de produtos vazia.\n")
    else:
        print("\nLista de produtos:")
    for produto in lista:
        print(f"Nome: {produto['Nome']}, Preço: {produto['Preço']}, Quantidade: {produto['Quantidade']}")
        print()


lista_produtos = []

while True:
    print("Selecione a opção abaixo:")
    print("1 - Cadastrar produtos")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Opção: ")

    if opcao == '1':
        cadastrar_produto(lista_produtos)
    elif opcao == '2':
        listar_produtos(lista_produtos)
    elif opcao == '3':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")




