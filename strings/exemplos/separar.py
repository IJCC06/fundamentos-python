def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

nome_completo = input("Digite seu nome completo: ")
print(f'Nome em partes: {separar_nome(nome_completo)}')