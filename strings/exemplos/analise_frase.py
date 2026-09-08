def analisar_frase(frase, palavra):
    frase_limpa = frase.strip().lower()

    qtde_caracteres = len(frase_limpa)
    qtde_palavras = len(frase_limpa.split())
    ocorrencia_palavra = frase_limpa.count(palavra.lower())

    print(f"Frase Completa: {frase_limpa}")
    print(f"Total de Caracteres: {qtde_caracteres}")
    print(f"Quantidade de Palavras: {qtde_palavras}")
    print(f"Ocorrências da palavra '{palavra}': {ocorrencia_palavra}")


frase = input("Digite uma frase: ")
ocorrencia_palavra = input("Digite uma palavra para contar sua ocorrência: ")
analisar_frase(frase, ocorrencia_palavra)