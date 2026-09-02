def procurar_palavra(texto, palavra):
    palavra_no_texto = palavra.lower() in texto.lower().strip()

    if palavra_no_texto:
        posicao = texto.lower().find(palavra.lower())
        print(f"Palavra Encontrada!")
        print(f"Posição: {posicao}")
    else:
        print("Palavra não encontrada")

texto = input("Digite um texto: ")
palavra = input("Digite a palavra a ser encontrada: ")
procurar_palavra(texto, palavra)