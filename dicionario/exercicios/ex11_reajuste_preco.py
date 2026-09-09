def reajustar_preco():
    produto = {
        "nome": "Mouse",
        "preco": 80.0,
        "estoque": 10
    }

    print(f"Preço Atual: R$ {produto["preco"]}")

    aumento = int(input("Digite o aumento em porcentagem: "))
    print(f"Aumento: {aumento}%")

    produto["preco"] *= 1 + (aumento / 100)
    print(f"Novo Preço: R$ {produto["preco"]}")

reajustar_preco()