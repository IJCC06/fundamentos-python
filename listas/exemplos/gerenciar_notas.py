def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    notas_ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return notas_ordenadas, media


lista_de_notas = [5.5, 4.5, 9, 10, 8.5]

notas_ordenadas, media = gerenciar_notas(lista_de_notas, 6.7)
print(f"Suas notas são {notas_ordenadas}")
print(f"Sua média é {media:.2f}")