def controle_de_estoque():
    produto = {
        "nome": "Mouse",
        "preco": 80,
        "estoque": 10
    }

    quantidade_vendida = int(input(f"Digite a quantidade de {produto["nome"]} vendidos: "))

    if quantidade_vendida > produto["estoque"]:
        print("Quantidade Insuficiente!")
        print(f"Estoque Atual: {produto["estoque"]}")
    else:
        produto["estoque"] -= quantidade_vendida
        print(f"Estoque: {produto["estoque"]}")

controle_de_estoque()