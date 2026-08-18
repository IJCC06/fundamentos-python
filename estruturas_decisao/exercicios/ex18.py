def calculadora_frete():
    valor_compra = float(input("Digite o valor da compra: "))

    if valor_compra <= 100:
        valor_frete = 20
    elif 100 < valor_compra <= 300:
        valor_frete = 10
    elif valor_compra > 300:
        valor_frete = 0

    total = valor_compra + valor_frete
    print(f"O total é de R$ {total}")

calculadora_frete()