def contar_palavras(texto):
    qtde_palavras = len(texto.split())
    print(f"Número de Palavras: {qtde_palavras}")

texto = input("Digite o texto: ")
contar_palavras(texto)