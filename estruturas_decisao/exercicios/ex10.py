def desconto():
    valor_da_compra = round(float(input("Digite o valor da compra: ")), 2)

    if valor_da_compra <= 100:
        print("=== Valor Total ===")
        print("Desconto = R$ 0,00")
        print(f"Valor = R$ {valor_da_compra}")

    elif 100 < valor_da_compra <= 500:
        desconto = round(valor_da_compra * 0.1, 2)
        valor_total = valor_da_compra - desconto

        print("=== Valor Total ===")
        print(f"Desconto = R$ {desconto}")
        print(f"Valor = R$ {valor_total}")

    elif valor_da_compra > 500:
        desconto = round(valor_da_compra * 0.15, 2)
        valor_total = valor_da_compra - desconto

        print("=== Valor Total ===")
        print(f"Desconto = R$ {desconto}")
        print(f"Valor = R$ {valor_total}")

    else:
        print("Valor Inválido")

desconto()