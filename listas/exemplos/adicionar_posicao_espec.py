def adicionar_nome_posicao(nome, nomes, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} da lista {nomes}")
    print(nomes)

lista_de_nomes = ["Gabriel", "João", "Lula", "Vorcaro"]
adicionar_nome_posicao("Luiz", lista_de_nomes, 3)