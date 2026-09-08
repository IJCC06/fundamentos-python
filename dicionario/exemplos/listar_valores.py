def listar_valores():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for valor in produto.values():
        print(valor)

listar_valores()