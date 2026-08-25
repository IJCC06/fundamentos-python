def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Nome não encontrado!")
    else:
        posicao = nomes.index(nome)
        print(f"A posição do nome {nome} é {posicao}")

lista_de_nomes = ["Gabriel", "João", "Lula", "Vorcaro", "Luiz", "Carlos"]
encontrar_posicao_pelo_valor(lista_de_nomes, "Gabriel")