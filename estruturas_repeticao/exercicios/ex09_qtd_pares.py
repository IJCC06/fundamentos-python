def quantidade_de_pares():
    contador = 0
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: ")) + 1

    for i in range(inicio, fim):
        if (i % 2) == 0:
            contador += 1
    print(f"Têm {contador} pares")

quantidade_de_pares()