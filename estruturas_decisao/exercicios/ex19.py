def classificacao_numero():
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        classe_1 = "Positivo"
    elif numero < 0:
        classe_1 = "Negativo"
    elif numero == 0:
        classe_1 = ""

    if (numero % 2) == 0:
        classe_2 = "Par"
    else:
        classe_2 = "Ímpar"

    print(f"Número: {numero}")
    print(f"Classificação: {classe_1} e {classe_2}")

classificacao_numero()