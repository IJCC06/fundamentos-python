def limpar_texto(texto):
    print(f"Texto antes: {texto}")
    print(f"Texto depois: {texto.strip()}")

texto = input("Digite um texto: ")
limpar_texto(texto)