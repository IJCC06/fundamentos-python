def exibir_numeros_primos():
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: ")) + 1

    for numero in range(inicio, fim):
        if numero < 2:
            continue

        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

        if primo:
            print(numero)

exibir_numeros_primos()