def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    return posicao


produtos = ["Mouse", "Teclado", "Monitor", "Webcam"]

print(encontrar_produto(produtos, "Monitor"))