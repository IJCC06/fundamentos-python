estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]


def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print("Produto vendido:", produto)
    else:
        print("Produto não está disponível.")

    return estoque


print(vender_produto(estoque, "RAM"))