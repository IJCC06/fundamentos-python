def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    return palavra_presente

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

print(f"A palavra está presente na frase? {verificar_palavra(frase, palavra)}")