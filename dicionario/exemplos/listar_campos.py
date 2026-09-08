def listar_campos():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for chave in produto.keys():
        print(chave)

listar_campos()