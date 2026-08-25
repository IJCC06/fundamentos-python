def maior_numero():
    maior = None

    while True:
        numero = float(input("Digite um número: "))

        if maior is None or numero > maior:
            maior = numero

        continuar = input("Deseja informar outro número? (s/n): ")

        if continuar.lower() != "s":
            break

    return maior

print(maior_numero())