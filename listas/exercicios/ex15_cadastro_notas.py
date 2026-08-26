def adicionar_nota(notas, nota):
    notas.append(nota)


def remover_nota(notas, nota):
    notas.remove(nota)


def media_notas(notas):
    return sum(notas) / len(notas)


notas = [7.5, 8.0, 6.5]

adicionar_nota(notas, 9.0)

print("Notas:", notas)

remover_nota(notas, 8.0)

print("Notas após remoção:", notas)

print("Média:", media_notas(notas))