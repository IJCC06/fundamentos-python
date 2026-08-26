def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valor = produto[1] * produto[2]
        valores.append(valor)

    return sum(valores)


lista_produtos = [
    ["Arroz", 1, 32.00],
    ["Café", 2, 23.00],
    ["Macarrão", 3, 13.00]
]
preco_total = valor_total_produtos(lista_produtos)
print(f"O valor total dos produtos é {preco_total}")