def validar_telefone(numeros):
    telefone_valido = numeros.isdigit()

    print(f"Entrada: {numeros}")
    if telefone_valido:
        print("Número de Telefone Válido!")
    else:
        print("Número inválido! Digite somente números.")

numeros = input("Digite seu número de telefone: ")
validar_telefone(numeros)