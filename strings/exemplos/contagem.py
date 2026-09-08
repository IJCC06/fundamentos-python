def analisar_texto(texto, letra):
    # Contar os caracteres
    qtde_caracteres = len(texto)
    # Contar a quantidade de ocorrencias
    qtde_letra = texto.strip().lower().count(letra)

    return qtde_caracteres, qtde_letra

texto = input("Digite um texto: ")
letra = input("Digite uma letra: ")
qtde_caracteres, qtde_letra = analisar_texto(texto, letra)

print(f"Número de Caracteres = {qtde_caracteres}")
print(f"Número de Letras '{letra}' = {qtde_letra}")