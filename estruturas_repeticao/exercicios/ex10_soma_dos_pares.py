def soma_dos_pares():
    total = 0
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: ")) + 1

    for num in range(inicio, fim):
        if (num % 2) == 0:
            total += num
    print(f"O total dos números pares é {total}")

soma_dos_pares()