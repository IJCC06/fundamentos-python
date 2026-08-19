def contagem_regressiva():
    numero = int(input("Digite o número inicial da contagem: "))
    while numero > 0:
        print(numero)
        numero -= 1
    print("FIM")

contagem_regressiva()