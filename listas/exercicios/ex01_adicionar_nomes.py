def adicionar_nomes(nomes, nome):
    nomes.append(nome)
    print(f"O nome {nome} foi adicionado a {nomes}")

lista_de_nomes = ["Gabriel", "Lucas", "João", "Maria"]
novo_nome = input("Digite o nome a ser adicionado: ")

adicionar_nomes(lista_de_nomes, novo_nome)