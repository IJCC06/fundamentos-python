def lista_de_compras():
    compra = {
        "cliente": "Maria",
        "produtos": []
    }

    for produto in range(5):
        compra["produtos"].append(input(f"Digite o produto {produto + 1}: "))

    print("Lista de Compras:")
    print(f"Cliente: {compra["cliente"]}")
    print(f"Produtos: {compra["produtos"]}")

lista_de_compras()