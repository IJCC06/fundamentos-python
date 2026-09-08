def exibir_produto():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for chave, valor in produto.items():
        print(f"A chave {chave} possui o valor: {valor}")

exibir_produto()