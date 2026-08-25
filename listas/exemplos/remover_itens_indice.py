def remover_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome {nomes[posicao]} foi removido da lista {nomes}")


lista_de_nomes = ["Gabriel", "João", "Lula", "Vorcaro", "Luiz", "Carlos"]
remover_pelo_indice(lista_de_nomes, 3)