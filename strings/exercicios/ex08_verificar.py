def verificar_palavra(texto, palavra):
    palavra_no_texto = palavra.lower() in texto.lower().strip()

    if palavra_no_texto:
        print(f"Palavra Encontrada!")
    else:
        print("Palavra não encontrada")


texto = input("Digite um texto: ")
palavra = input("Digite a palavra a ser encontrada: ")
verificar_palavra(texto, palavra)