def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)

    return total / quantidade


notas = [7, 8, 9, 10]

print(calcular_media(notas))