def remover_produto(produtos, produto):
    if produto not in produtos:
        print("Produto não Encontrado")
    else:
        produtos.remove(produto)
        print(f"O produto {produto} foi removido")
        print(f"Nova lista de produtos: {produtos}")


lista_de_produtos = ["Café", "Arroz", "Açúcar"]
novo_produto = input("Digite o novo produto: ")

remover_produto(lista_de_produtos, novo_produto)