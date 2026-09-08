def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

print(f"A posição da palavra {palavra} é {encontrar_posicao_palavra(frase, palavra)}")