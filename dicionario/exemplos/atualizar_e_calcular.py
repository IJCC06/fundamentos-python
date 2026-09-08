def atualizar_estoque():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    produto["total"] = produto["quantidade"] * produto["preco_unitario"]
    print(f"Total = R$ {produto["total"]}")

atualizar_estoque()