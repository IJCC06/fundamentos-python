def consumo_energia():
    consumo = float(input("Digite seu consumo em kWh: "))
    preco = float(input("Digite o valor do kWh: "))
    valor_da_conta = consumo * preco
    print(f"O valor da conta é de R$ {valor_da_conta}")

consumo_energia()