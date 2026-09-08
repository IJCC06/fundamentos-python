def listar_produtos():
    produtos = [
        {"nome": "Teclado", "preco": 299.00, "quantidade": 2},
        {"nome": "Mouse", "preco": 25.00, "quantidade": 3},
        {"nome": "Monitor", "preco": 1200.00, "quantidade": 1}
    ]

    total = 0
    for produto in produtos:
        print(f"O produto {produto["nome"]} custa R$ {produto["preco"]}")
        total += produto["preco"] * produto["quantidade"]
    print(f"Total de Produtos = R$ {total}")

listar_produtos()