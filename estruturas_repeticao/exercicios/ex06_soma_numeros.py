def somar_ate():
    numero = int(input("Digite um número: ")) + 1
    total = 0
    for i in range(1, numero):
        total += i

    print(f"O total é {total}")

somar_ate()