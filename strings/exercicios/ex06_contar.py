def contar_letra(frase, letra):
    qtde_da_letra = frase.count(letra)

    print(f"Frase: {frase}")
    print(f"Quantidade de letras '{letra}': {qtde_da_letra}")

frase = input("Digite uma frase: ")
letra = input("Digite qual letra você quer verificar a ocorrência: ")
contar_letra(frase, letra)