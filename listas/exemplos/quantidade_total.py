def quantidade_total_produtos(produtos):
    quantidades = []

    for produto in produtos:
        quantidades.append(produto[1])

    return sum(quantidades)


lista_produtos = [
    ["Arroz", 1, 32.00],
    ["Café", 2, 23.00],
    ["Macarrão", 3, 13.00]
]

quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f"A quantidade total de produtos é {quantidade_produtos}")