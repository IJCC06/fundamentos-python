def separar_nome(nome_completo):
    nome_separado = nome_completo.split()

    print(f"Entrada: {nome_completo}")
    print("Saída:")
    for nome in nome_separado:
        print(nome)

nome = input("Digite seu nome completo: ")
separar_nome(nome)