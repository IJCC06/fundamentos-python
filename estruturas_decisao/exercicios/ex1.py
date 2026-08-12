def avaliador_numero():
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        print(f"O número {numero} é positivo!")
    elif numero < 0:
        print(f"O número {numero} é negativo!")
    else:
        print("Esse é o 0!")

avaliador_numero()