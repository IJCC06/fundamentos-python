def formatar_nome(nome):
    # Maiúsculo
    nome_maiusculo = nome.upper()
    # Minúsculo
    nome_minusculo = nome.lower()
    # 1ª Letra Maiúscula
    nome_primeira_maiuscula = nome.capitalize()

    return nome_maiusculo, nome_minusculo, nome_primeira_maiuscula

nome = input("Digite seu nome: ")

nome_maiusculo, nome_minusculo, nome_primeira_maiuscula = formatar_nome(nome)
print(f"Nome Maiúsculo: {nome_maiusculo}")
print(f"Nome Minúsculo: {nome_minusculo}")
print(f"Primeira Letra Maiúscula: {nome_primeira_maiuscula}")