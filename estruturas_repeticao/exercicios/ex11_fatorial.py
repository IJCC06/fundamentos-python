def fatorial():
    numero = int(input("Digite um número: "))
    resultado = 1

    for i in range(numero, 0, -1):
        resultado *= i

    print(resultado)

fatorial()