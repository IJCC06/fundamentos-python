def remover_da_lista(nome, nomes):
    if nome not in nomes:
        print("Esse nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido da lista {nomes}")


lista_de_nomes = ["Gabriel", "João", "Lula", "Vorcaro"]
remover_da_lista("Cris", lista_de_nomes)