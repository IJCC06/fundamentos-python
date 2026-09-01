def validar_nome(nome):
    nome_valido = nome.isalpha()
    if nome_valido:
        print("Nome Válido")
    else:
        print("O nome deve conter somente letras")

nome = input("Digite seu nome: ")
validar_nome(nome)