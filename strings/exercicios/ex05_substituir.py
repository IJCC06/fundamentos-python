def substituir_palavra(frase, palavra_1, palavra_2):
    frase_nova = frase.replace(palavra_1, palavra_2)
    print(f"Frase: {frase}")
    print(f"Palavra Antiga: {palavra_1}")
    print(f"Palavra Nova: {palavra_2}")
    print(f"Saída: {frase_nova}")

frase = input("Digite uma frase: ")
palavra_1 = input("Digite qual palavra que remover: ")
palavra_2 = input("Digite a nova palavra: ")
substituir_palavra(frase, palavra_1, palavra_2)