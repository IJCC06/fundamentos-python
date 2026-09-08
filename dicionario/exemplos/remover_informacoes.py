def remover_informacoes():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    # Apaga a Chave
    del produto["nome"]
    # Apaga e armazena em outro varíavel
    preco_unitario = produto.pop("preco_unitario")

    print(produto, preco_unitario)

remover_informacoes()