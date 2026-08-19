def soma_com_while():
    while True:
        num_1 = int(input("Digite o primeiro número: "))
        num_2 = int(input("Digite o segundo número: "))

        if num_1 == 0:
            print("Função de Soma Encerrada!")
            break
        else:
            soma = num_1 + num_2
            print(f"O resultado da soma é {soma}")

soma_com_while()