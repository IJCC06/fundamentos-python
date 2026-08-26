def adicionar_produto(produtos, produto):
    produtos.append(produto)
    print(f"Minha lista de produtos: {produtos[2]}")


lista_produtos = [
    ["Arroz", 2, 32.00],
    ["Café", 2, 23.00]
]
novo_produto = ["Macarrão", 3, 13.00]

adicionar_produto(lista_produtos, novo_produto)